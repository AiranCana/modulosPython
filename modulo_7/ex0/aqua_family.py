from .creature import Creature, CreatureFactory


class Aquabub(Creature):
    def __init__(self, name: str, types: str) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self._name} use Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str, types: str) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self._name} use Water Pump!"


class AquaFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> Creature:
        return Torragon("Torragon", "Water")
