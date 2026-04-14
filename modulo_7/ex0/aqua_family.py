from .creature import Creature, CreatureFactory


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__()
        self._type = "Water"
        self._name = "Aquabub"

    def attack(self) -> str:
        return f"{self._name} use Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self._type = "Water"
        self._name = "Torragon"

    def attack(self) -> str:
        return f"{self._name} use Water Pump!"


class AquaFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
