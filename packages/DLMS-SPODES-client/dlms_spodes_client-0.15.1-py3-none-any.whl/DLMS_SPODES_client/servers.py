from dataclasses import dataclass, field
from typing import Optional
from threading import Thread, Event
from functools import cached_property
import asyncio
from StructResult import result
from DLMSCommunicationProfile.osi import OSI
from DLMS_SPODES.config_parser import get_values
from .logger import LogLevel as logL
from .client import Client, Errors
from . import task

_setting = {
    "depth": 10
}
if toml_val := get_values("DLMSClient", "session", "results"):
    _setting.update(toml_val)


@dataclass(eq=False)
class Session:
    c: Client
    complete: bool = False
    errors: Errors = field(default_factory=Errors)  # todo: remove in future, replace to <err>
    res: result.Result = field(init=False)

    async def run(self, t: task.ExTask):
        self.c.lock.acquire(timeout=10)  # 10 second, todo: keep parameter anywhere
        assert self.c.media is not None, F"media is absense"  # try media open
        self.res = await t.run(self.c)
        self.c.lock.release()
        self.complete = True
        if results is not None:
            keep_result(self)
        self.errors = self.c.errors
        # media close
        if not self.c.lock.locked():
            self.c.lock.acquire(timeout=1)
            if self.c.media.is_open():
                self.c.log(logL.DEB, F"close communication channel: {self.c.media}")
                await self.c.media.close()
            else:
                self.c.log(logL.WARN, F"communication channel: {self.c.media} already closed")
            self.c.lock.release()
            self.c.level = OSI.NONE
        else:
            """opened media use in other session"""

    def __hash__(self):
        return hash(self.c)


class Sessions:
    __non_complete: set[Session]
    __complete: set[Session]
    name: str
    tsk: task.Base

    def __init__(self, clients: tuple[Client],
                 tsk: task.Base,
                 name: str = None):
        self.__non_complete = {Session(c) for c in clients}
        self.__complete = set()
        self.tsk = tsk
        self.name = name
        """common operation name"""

    @cached_property
    def all(self) -> set[Session]:
        return self.__non_complete | self.__complete

    def __getitem__(self, item) -> Session:
        return tuple(self.all)[item]

    @cached_property
    def clients(self) -> set[Client]:
        return {sess.c for sess in self.all}

    @property
    def ok_results(self) -> set[Session]:
        """without errors exchange clients"""
        return {sess for sess in self.__complete if sess.res.err is None}

    @cached_property
    def nok_results(self) -> set[Session]:
        """ With errors exchange clients """
        return self.all.difference(self.ok_results)

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

    async def coro_loop(self, sessions: Sessions, abort_timeout: int):
        async def check_stop(tg: asyncio.TaskGroup):
            while True:
                await asyncio.sleep(abort_timeout)
                if sessions.is_complete():
                    break
                elif self.__stop.is_set():
                    tg._abort()
                    break

        async with asyncio.TaskGroup() as tg:
            for sess in sessions:
                # tg.create_task(
                    # coro=session(
                    #     c=res.client,
                    #     t=results.tsk,
                    #     result=res))
                tg.create_task(sess.run(sessions.tsk))
            tg.create_task(
                coro=check_stop(tg),
                name="wait abort task")


if _setting.get("depth") > 0:
    from collections import deque

    results: Optional[dict[Client, deque[result.Result]]] = dict()
    """exchange results archive"""


    def keep_result(sess: Session):
        global results
        if (entries := results.get(sess.client)) is None:
            results[sess.client] = (entries := deque())
        if _setting["depth"] <= len(entries):
            entries.popleft()
        entries.append(sess.res)
else:
    results = None
