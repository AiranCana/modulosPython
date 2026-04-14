from .creature import Creature, CreatureFactory


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__()
        self._type = "Fire"
        self._name = "Flameling"

    def attack(self) -> str:
        return f"{self._name} use Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self._type = "Fire/Flying"
        self._name = "Pyrodon"

    def attack(self) -> str:
        return f"{self._name} use Flamethrower!"


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()
