#!/usr/bin/env python3
class PlantError(Exception):
    def __init__(self, args: str = "lettuce"):
        super().__init__(f"Invalid plant name to water: '{args}'")


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(plant_name)


def test_watering_system() -> None:
    valid = ["Tomato", "Lettuce", "Carrots"]
    valid1 = ["Tomato", "lettuce", "Carrots"]
    testing = [valid, valid1]
    hola = "valid"
    print("=== Garden Watering System ===", end="\n\n")
    for i in testing:
        try:
            print(f"\nTesting {hola} plants...")
            if hola == "valid":
                hola = "invalid"
            print("Opening watering system")
            for veg in i:
                water_plant(veg)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
            print(".. ending tests and returning to main")
            break
        finally:
            print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
