from ex0 import Creature, CreatureFactory
from .capabilities import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, types: str) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        if self._transformer:
            return f"{self._name} performs a boosted strike!"
        else:
            return f"{self._name} attacks normally."

    def transform(self) -> str:
        if self._transformer:
            return f"{self._name} has already changed."
        else:
            self._transformer = True
            return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        if self._transformer:
            self._transformer = False
            return f"{self._name} returns to normal."
        else:
            return f"{self._name} is in normal form."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, types: str) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        if self._transformer:
            return f"{self._name} unleashes a devastating morph strike!"
        else:
            return f"{self._name} attacks normally."

    def transform(self) -> str:
        if self._transformer:
            return f"{self._name} has already changed."
        else:
            self._transformer = True
            return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        if self._transformer:
            self._transformer = False
            return f"{self._name} stabilizes its form."
        else:
            return f"{self._name} is in normal form."


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Morphagon", "Normal/Dragon")
