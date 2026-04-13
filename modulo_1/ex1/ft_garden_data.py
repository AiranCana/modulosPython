#!/usr/bin/env python3
class Plants:

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        c = f"{self.name}: "
        c += f" {self.height}cm, {self.age} days old"
        print(c)


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    hola = Plants("Rose", 25, 30)
    adios = Plants("Sunflower", 80, 45)
    como = Plants("Cactus", 15, 120)
    for s in (hola, como, adios):
        s.show()
