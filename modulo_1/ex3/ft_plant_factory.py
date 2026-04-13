#!/usr/bin/env python3
class Plants:

    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        c = f"{self.name}: "
        c += f" {self.height:.1f}cm, {self.days} days old"
        print(c)

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    planta0 = Plants("Rosa", 25, 30)
    planta1 = Plants("Oak", 200, 365)
    planta2 = Plants("Cactus", 5, 90)
    planta3 = Plants("Sunflowersa", 80, 45)
    planta4 = Plants("Fern", 15, 120)
    for p in (planta0, planta1, planta2, planta3, planta4):
        print("Create: ", end="")
        p.show()
