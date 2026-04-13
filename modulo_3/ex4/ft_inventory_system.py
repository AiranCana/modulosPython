#!/usr/bin/env python3
import sys


inventary: dict[str, int] = {}


def mysplit(stri: str, sep: str = '/') -> list[str]:
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


def found(stri: str) -> bool:
    for i in stri:
        if i == ':':
            return True
    return False


def getVal(stri: str) -> list[str]:
    result: list[str] = []
    current = ""

    for let in stri:
        if let == ':':
            result = result + [current]
            current = ""
        else:
            current += let
    result = result + [current]
    return result


def found_inventory(stri: str) -> bool:
    for i in inventary:
        if i == stri:
            return True
    return False


def asign_invetori(argv: list[str]) -> None:
    for i in argv[0:]:
        if not found(i):
            print(f"Error - invalid parameter '{mysplit(i)[-1]}'")
        elif found_inventory(getVal(i)[0]):
            print(f"Redundant item '{getVal(i)[0]}' - discarding")
        else:
            key_val = getVal(i)
            try:
                j = int(key_val[1])
                if j <= 0:
                    raise Exception
                inventary.update({key_val[0]: j})
            except Exception as e:
                print(f"Quantity error for '{key_val[0]}': {e}")


def getObject() -> list[str]:
    lis = []
    for i in inventary:
        lis += [i]
    return lis


def optenfull() -> int:
    s = 0
    for i in inventary:
        s += inventary[i]
    return s


def limits() -> tuple[dict[str, int], dict[str, int]]:
    mini = {"hola": 100000000}
    maxi = {"hola": 0}
    for i, v in inventary.items():
        M, *_ = maxi.keys()
        m, *_ = mini.keys()
        if maxi[M] < v:
            maxi = {i: v}
        if mini[m] > v:
            mini = {i: v}
    return maxi, mini


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    asign_invetori(sys.argv)
    print(f"Got inventory: {inventary}")
    objec = getObject()
    print(f"Item list: {objec}")
    s = len(objec)
    full = optenfull()
    print(f"Total quantity of the {s} items: {full}")
    for i, v in inventary.items():
        print(f"Item {i} represents {((v/full)*100):.1f}%")
    if len(sys.argv[1:]) > 0 and s >= 1:
        maxi, mini = limits()
        keyM, *_ = maxi.keys()
        keym, *_ = mini.keys()
        print(f"Item most abundant: {keyM} with quantity {maxi[keyM]}")
        print(f"Item least abundant: {keym} with quantity {mini[keym]}")
    inventary.update({"magic_item": 1})
    print(f"Updated inventory: {inventary}")
