#!/usr/bin/env python3
import sys
from typing import IO


def lectura(file: str) -> None:
    try:
        fd = open(file, "r")
        print("---", end="\n\n")
        print(fd.read(), end="\n\n")
        print("---")
        IO.close(fd)
        print(f"file {file} closed")
    except IOError as e:
        print(f"Error opening file '{file}': {e}")


def mysplit(s: str) -> list[str]:
    resul = []
    c = ""
    for i in s:
        if i == '\\':
            resul += [c]
            c = ""
        else:
            c += i
    resul += [c]
    return resul


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 1:
        print(f"Usage: {mysplit(sys.argv[0])[-1]} <file>")
    else:
        file = sys.argv[-1]
        print(f"Accessing file '{file}'")
        lectura(file)
