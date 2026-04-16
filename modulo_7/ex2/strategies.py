from abc import ABC, abstractmethod
from ex0 import Creature
from ex1.capabilities import HealCapability, TransformCapability
from typing import Any, cast


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, criature: Any) -> str:
        ...

    @abstractmethod
    def is_valid(self, criature: Any) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, criature: Any) -> str:
        cri = cast(Creature, criature)
        if self.is_valid(criature):
            return cri.attack()
        raise TypeError(f"Invalid Creature '{cri._name}' for this normal" +
                        " strategy")

    def is_valid(self, criature: Any) -> bool:
        return isinstance(criature, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, criature: Any) -> str:
        cri = cast(Creature, criature)
        c: str = ""
        if self.is_valid(criature):
            cri2 = cast(TransformCapability, criature)
            c += cri2.transform()
            c += "\n"
            c += cri.attack()
            c += "\n"
            c += cri2.revert()
            return c
        raise TypeError(f"Invalid Creature '{cri._name}' for this aggressive" +
                        " strategy")

    def is_valid(self, criature: Any) -> bool:
        return (isinstance(criature, TransformCapability) and
                isinstance(criature, Creature))


class DefensiveStrategy(BattleStrategy):
    def act(self, criature: Any) -> str:
        cri = cast(Creature, criature)
        c: str = ""
        if self.is_valid(criature):
            cri2 = cast(HealCapability, criature)
            c += cri.attack()
            c += "\n"
            c += cri2.heal()
            return c
        raise TypeError(f"Invalid Creature '{cri._name}' for this defensive" +
                        " strategy")

    def is_valid(self, criature: Any) -> bool:
        return (isinstance(criature, HealCapability) and
                isinstance(criature, Creature))
