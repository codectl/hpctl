from abc import ABC, abstractmethod


class SchedulerBase(ABC):

    def __init__(self, exec, server=None):
        self._exec = exec
        self.server = server

    @abstractmethod
    def nodes(self, server=None):
        """Provide metrics on each node of the cluster."""
        raise NotImplementedError
