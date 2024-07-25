from abc import ABC, abstractmethod


class BaseError(Exception, ABC):
    @property
    @abstractmethod
    def message(self) -> str: ...

    def __str__(self) -> str:
        return self.message
