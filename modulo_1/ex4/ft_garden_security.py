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

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age += 1

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


if __name__ == "__main__":
    planta = Plants("Rosa", 25, 8)
    planta.set_age(-2)
    print()
    planta.set_age(30)
    print()
    planta.set_height(-2)
    print()
    planta.set_height(10)
    print()
