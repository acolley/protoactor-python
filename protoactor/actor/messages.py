from abc import ABCMeta
from typing import Optional, Any

from protoactor.actor.protos_pb2 import PID
from protoactor.actor.restart_statistics import RestartStatistics
from protoactor.actor.utils import Singleton


class AbstractSystemMessage():
    pass

class AbstractNotInfluenceReceiveTimeout(metaclass=ABCMeta):
    pass

class AutoReceiveMessage(metaclass=ABCMeta):
    pass


class Restarting(metaclass=Singleton):
    pass


class Restart(AbstractSystemMessage):
    def __init__(self, reason):
        self.reason = reason


class Failure(AbstractSystemMessage):
    def __init__(self, who: PID, reason: Exception, crs: RestartStatistics, message: Any) -> None:
        self._who = who
        self._reason = reason
        self._crs = crs
        self._message = message

    @property
    def who(self) -> PID:
        return self._who

    @property
    def reason(self) -> Exception:
        return self._reason

    @property
    def restart_statistics(self) -> RestartStatistics:
        return self._crs

    @property
    def message(self) -> Any:
        return self._message


class SystemMessage:
    pass


class Stopping(AutoReceiveMessage):
    pass


class Stopped(AutoReceiveMessage):
    pass


class Started(AbstractSystemMessage):
    pass


class ReceiveTimeout(AbstractSystemMessage, metaclass=Singleton):
    pass


class NotInfluenceReceiveTimeout(AbstractSystemMessage):
    pass


class PoisonPill(AbstractSystemMessage):
    pass


class Continuation(SystemMessage):
    def __init__(self, fun, message):
        self.action = fun
        self.message = message


class SuspendMailbox(SystemMessage):
    pass


class ResumeMailbox(SystemMessage):
    pass


class DeadLetterEvent:
    def __init__(self, pid: 'PID', message: object, sender: Optional['PID']) -> None:
        self._pid = pid
        self._message = message
        self._sender = sender

    @property
    def pid(self) -> 'PID':
        return self._pid

    @property
    def message(self) -> object:
        return self._message

    @property
    def sender(self) -> Optional['PID']:
        return self._sender
