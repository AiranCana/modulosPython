#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, args: str = "Unknown plant error"):
        super().__init__(args)


class PlantError(GardenError):
    def __init__(self, str: str = "tomato"):
        super().__init__(f"The {str} plant is wilting!")


class WaterError(GardenError):
    def __init__(self) -> None:
        super().__init__("Not enough water in the tank!")


def prube() -> None:
    print("=== Custom Garden Errors Demo ===", end="\n\n")
    print("Testing PlantError...")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("Testing WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"\nCaught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise GardenError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    prube()
    print("\nAll custom error types work correctly!")
