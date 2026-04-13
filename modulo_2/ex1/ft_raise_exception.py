#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    i = int(temp_str)
    if i > 40:
        raise ValueError(f"{i}ºC is too hot for plants (max 40ºC)")
    elif i < 0:
        raise ValueError(f"{i}ºC is too cold for plants (min 0ºC)")
    return i


def test_temperature() -> None:
    num = "25"
    leter = "abc"
    maxi = "100"
    mini = "-50"
    print("=== Garden Temperature ===")
    for data in (num, leter, maxi, mini):
        try:
            print(f"\nInput data is {data}")
            i = input_temperature(data)
            print(f"Temperature is now {i}ºC")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
