#!/usr/bin/env python3
import math


def mysplit(stri: str, sep: str = ',') -> list[str]:
    result: list[str] = []
    current = ""

    for let in stri:
        if let == sep:
            result = result + [current]
            current = ""
        else:
            current += let
    result = result + [current]
    return result


def get_player_pos() -> tuple[float, ...]:
    while (True):
        a = input("Enter new coordinates asfloats in format 'x,y,z'")
        lists = mysplit(a)
        if (len(lists) == 3):
            try:
                result = [round(float(i), 1) for i in lists]
                return tuple(result)
            except ValueError as e:
                srr = e.args[0]
                print(f"Error in param {srr[35:]}: {e}")
        else:
            print("Invalid syntax")


def main() -> None:
    print("=== Game Coordinate System ===", end="\n\n")
    print("Get first set coordinates")
    x1, y1, z1 = get_player_pos()
    print(f"Got the first tuple: ({x1}, {y1}, {z1})")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    result = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(result, 4)}")
    x2, y2, z2 = get_player_pos()
    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(result, 4)}")


if __name__ == "__main__":
    main()
