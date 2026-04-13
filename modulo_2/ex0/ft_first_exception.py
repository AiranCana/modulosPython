#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    num = "25"
    leter = "abc"
    print("=== Garden Temperature ===")
    for data in (num, leter):
        try:
            print(f"\nInput data is {data}")
            i = input_temperature(data)
            print(f"Temperature is now {i}ºC")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
