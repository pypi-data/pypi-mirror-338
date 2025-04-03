from dataclasses import dataclass, field
from typing import Optional, Any
from threading import Thread, Event
from functools import cached_property
import asyncio
from StructResult import result
from DLMSCommunicationProfile.osi import OSI
from .logger import LogLevel as logL
from .client import Client, Errors
from . import task


# todo: join with StructResult.Result
@dataclass(eq=False)
class Session:
    client: Client
    complete: bool = False
    """complete exchange"""
    errors: Errors = field(default_factory=Errors)  # todo: remove in future, replace to <err>
    res: result.Result = field(init=False)

    async def session(self, t: task.ExTask):
        self.client.lock.acquire(timeout=10)  # 10 second, todo: keep parameter anywhere
        assert self.client.media is not None, F"media is absense"  # try media open
        self.res = await t.run(self.client)
        self.client.lock.release()
        self.complete = True
        self.errors = self.client.errors
        # media close
        if not self.client.lock.locked():
            self.client.lock.acquire(timeout=1)
            if self.client.media.is_open():
                self.client.log(logL.DEB, F"close communication channel: {self.client.media}")
                await self.client.media.close()
            else:
                self.client.log(logL.WARN, F"communication channel: {self.client.media} already closed")
            self.client.lock.release()
            self.client.level = OSI.NONE
        else:
            """opened media use in other session"""

    def __hash__(self):
        return hash(self.client)


class Sessions:
    __non_complete: set[Session]
    __complete: set[Session]
    name: str
    tsk: task.ExTask

    def __init__(self, clients: tuple[Client],
                 tsk: task.ExTask,
                 name: str = None):
        self.__non_complete = {Session(c) for c in clients}
        self.__complete = set()
        self.tsk = tsk
        self.name = name
        """common operation name"""

    @cached_property
    def sres(self) -> set[Session]:
        return self.__non_complete | self.__complete

    def __getitem__(self, item) -> Session:
        return tuple(self.sres)[item]

    @cached_property
    def clients(self) -> set[Client]:
        return {sres.client for sres in self.sres}

    @property
    def ok_results(self) -> set[Session]:
        """without errors exchange clients"""
        return {sres for sres in self.__complete if sres.res.err is None}

    @cached_property
    def nok_results(self) -> set[Session]:
        """ With errors exchange clients """
        return self.sres.difference(self.ok_results)

    def pop(self) -> set[Session]:
        """get and move complete session"""
        to_move = {sres for sres in self.__non_complete if sres.complete}
        self.__complete |= to_move
        self.__non_complete -= to_move
        return to_move

    def is_complete(self) -> bool:
        """check all complete sessions. call <pop> before"""
        return len(self.__non_complete) == 0


class TransactionServer:
    __t: Thread
    sessions: Sessions

    def __init__(self,
                 clients: list[Client] | tuple[Client],
                 tsk: task.ExTask,
                 name: str = None,
                 abort_timeout: int = 1):
        self.sessions = Sessions(clients, tsk, name)
        # self._tg = None
        self.__stop = Event()
        self.__t = Thread(
            target=self.__start_coro,
            args=(self.sessions, abort_timeout))

    def start(self):
        self.__t.start()

    def abort(self):
        self.__stop.set()

    def __start_coro(self, sessions, abort_timeout):
        asyncio.run(self.coro_loop(sessions, abort_timeout))

    async def coro_loop(self, results: Sessions, abort_timeout: int):
        async def check_stop(tg: asyncio.TaskGroup):
            while True:
                await asyncio.sleep(abort_timeout)
                if results.is_complete():
                    break
                elif self.__stop.is_set():
                    tg._abort()
                    break

        async with asyncio.TaskGroup() as tg:
            for sres in results:
                # tg.create_task(
                    # coro=session(
                    #     c=res.client,
                    #     t=results.tsk,
                    #     result=res))
                tg.create_task(sres.session(results.tsk))
            tg.create_task(
                coro=check_stop(tg),
                name="wait abort task")
