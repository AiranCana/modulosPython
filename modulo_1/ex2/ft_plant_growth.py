#!/usr/bin/env python3
class Plants:

    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        c = f"{self.name}: "
        c += f" {self.height:.1f}cm, {self.age} days old"
        print(c)

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    plant = Plants("Rosa", 25, 30)
    k = plant.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.show()
        plant.grow()
        j = plant.height
    print(f"Growth this week: {round(j-k)}cm")
