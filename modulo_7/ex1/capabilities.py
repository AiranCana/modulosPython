from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: Creature | None = None) -> str:
        ...


class TransformCapability(ABC):

    transformer: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
