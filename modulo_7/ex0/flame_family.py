from .creature import Creature, CreatureFactory


class Flameling(Creature):
    def __init__(self, name: str, types: str) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self._name} use Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str, types: str) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self._name} use Flamethrower!"


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> Creature:
        return Pyrodon("Pyrodon", "Fire/Flying")
