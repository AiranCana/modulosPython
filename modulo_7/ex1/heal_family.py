from ex0 import Creature, CreatureFactory
from .capabilities import HealCapability


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, types: str) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self._name} use Vine Whip!"

    def heal(self, target: Creature | None = None) -> str:
        if target is None:
            return f"{self._name} heals itself for a small amount"
        else:
            return f"{self._name} heals {target._name} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, types: str) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self._name} use Petal Dance!"

    def heal(self, target: Creature | None = None) -> str:
        if target is None:
            return f"{self._name} heals itself and others for a large amount"
        else:
            return (f"{self._name} heals {target._name} and" +
                    " others for a large amount")


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Bloomelle:
        return Bloomelle("Bloomelle", "Grass/Fairy")
