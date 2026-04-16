from abc import ABC, abstractmethod
from ex0 import Creature


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: Creature | None = None) -> str:
        ...


class TransformCapability(ABC):

    _transformer: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
