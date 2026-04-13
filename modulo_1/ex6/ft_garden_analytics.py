#!/usr/bin/env python3
class Plants:

    class _PlantMaster:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0

        def record_grow(self) -> None:
            self._grow += 1

        def record_age(self) -> None:
            self._age += 1

        def record_show(self) -> None:
            self._show += 1

        def display(self) -> None:
            c = f"Stats: {self._grow} grow, {self._age} age, {self._show} show"
            print(c)

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age
        self._count = Plants._PlantMaster()

    @classmethod
    def unknown(cls) -> "Plants":
        return cls("Unknown plant", 0, 0)

    def show(self) -> None:
        self._count.record_show()
        c = f"{self._name}: "
        c += f" {self._height:.1f}cm, {self._age} days old"
        print(c)

    def grow(self, days: int = 1) -> None:
        self._count.record_grow()
        self._height += days

    def age(self, days: int = 1) -> None:
        self._count.record_age()
        self._age += days

    def set_height(self, height: int) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    @staticmethod
    def verifymetod(age: int) -> None:
        c = f"Is {age} days more than a year? -> "
        if age > 365:
            c += "True"
        else:
            c += "False"
        print(c)


class Flower(Plants):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color
        self._bloom = False

    def bloom(self) -> None:
        print(f"[asking the {self._name} to grow and bloom]")
        self._bloom = True
        self.show()

    def show(self) -> None:
        super().show()
        c = f"Color: {self._color}"
        if self._bloom:
            c += f"\n{self._name} is blooming beautifully!"
        else:
            c += f"\n{self._name} has not bloomed yet"
        print(c)


class Tree(Plants):

    class _TreeMaster(Plants._PlantMaster):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade = 0

        def display(self) -> None:
            super().display()
            print(f"{self._produce_shade} shade")

        def record_shade(self) -> None:
            self._produce_shade += 1

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self._count: Tree._TreeMaster = Tree._TreeMaster()
        self.__trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._count.record_shade()
        c = f"[asking the {self._name} to produce shade]"
        c += f"\nTree {self._name} now produces a shade of "
        c += f"{self._height:.1f}cm long and "
        c += f"{self.__trunk_diameter:.1f}cm wide."
        print(c)

    def show(self) -> None:
        super().show()
        c = f"Trunk diameter: {self.__trunk_diameter:.1f}cm"
        print(c)


class Vegetable(Plants):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.__nutritional_value = 0
        self.__harvest_season = harvest_season

    def show(self) -> None:
        super().show()
        c = f"Harvest season: {self.__harvest_season}"
        c += f"\nNutritional value: {self.__nutritional_value}"
        print(c)

    def grow(self, days: int = 1) -> None:
        print(f"[make {self._name} grow and age for {days} days]")
        super().grow(days)
        self.__nutritional_value += days


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str, seeds: int):
        super().__init__(name, height, age, color)
        self.__seeds = seeds

    def show(self) -> None:
        super().show()
        c = f"Seeds: {self.__seeds}"
        print(c)


def displayMethod(plant: Plants) -> None:
    plant.show()
    print(f"[statistics for {plant._name}]")
    plant._count.display()


if __name__ == "__main__":
    print("=== Garden statistics ===\n=== Check year-old")
    Plants.verifymetod(30)
    Plants.verifymetod(400)
    print("\n=== Flower")
    flor = Flower("Rosa", 15, 2, "red")
    displayMethod(flor)
    flor.bloom()
    displayMethod(flor)
    print("\n=== Tree")
    arbol = Tree("Oak", 200, 365, 5)
    displayMethod(arbol)
    arbol.produce_shade()
    arbol._count.display()
    print("\n=== Seed")
    semilla = Seed("Sunflower", 80, 45, "yellow", 0)
    semilla.show()
    semilla.grow(30)
    semilla.age(20)
    displayMethod(semilla)
    print("\n=== Anonymous")
    anonimo = Plants.unknown()
    displayMethod(anonimo)
