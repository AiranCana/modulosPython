from abc import ABC, abstractmethod


class Creature(ABC):

    _name: str
    _type: str

    def __init__(self, name: str, types: str):
        self._name = name
        self._type = types

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...
