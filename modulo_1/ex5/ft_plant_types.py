#!/usr/bin/env python3
class Plants:

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        c = f"{self._name}: "
        c += f" {self._height:.1f}cm, {self._age} days old"
        print(c)

    def grow(self, days: int = 1) -> None:
        self._height += (0.8*days)

    def age(self, days: int = 1) -> None:
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


class Flower(Plants):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.__color = color
        self.__bloom = False

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self.__bloom = True

    def show(self) -> None:
        super().show()
        c = f"Color: {self.__color}"
        if self.__bloom:
            c += f"\n{self._name} is blooming beautifully!"
        else:
            c += f"\n{self._name} has not bloomed yet"
        print(c)


class Tree(Plants):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.__trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
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
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.__nutritional_value = 0
        self.__harvest_season = harvest_season

    def show(self) -> None:
        super().show()
        c = f"\nHarvest season: {self.__harvest_season}"
        c += f"\nNutritional value: {self.__nutritional_value}"
        print(c)

    def grow(self, days: int = 1) -> None:
        print(f"[make {self._name} grow and age for {days} days]")
        super().grow(days)
        self.__nutritional_value += days


if __name__ == "__main__":
    flor = Flower("Rosa", 15, 6, "red")
    verdura = Vegetable("Tomate", 15, 6, "Abril")
    arbol = Tree("Oak", 200, 6, 50)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flor.show()
    flor.bloom()
    flor.show()
    print()
    print("=== Tree")
    arbol.show()
    arbol.produce_shade()
    print()
    print("=== Vegetable")
    verdura.show()
    verdura.grow(20)
    verdura.show()
