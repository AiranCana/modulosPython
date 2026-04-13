#!/usr/bin/env python3
import sys
from typing import IO


def lectura(file: str) -> str | None:
    try:
        fd = open(file, "r")
        print("---", end="\n\n")
        x = fd.read()
        print(x, end="\n\n")
        print("---")
        IO.close(fd)
        print(f"file {file} closed", end="\n\n")
        return x
    except IOError as e:
        print(f"Error opening file '{file}': {e}")
        return None


def mysplit(s: str) -> list[str]:
    resul = []
    c = ""
    for i in s:
        if i == "/":
            resul += [c]
            c = ""
        else:
            c += i
    resul += [c]
    return resul


def lectur_file() -> (str | None):
    if len(sys.argv) == 1:
        print(f"Usage: {mysplit(sys.argv[0])[-1]} <file>")
        return None
    else:
        file = sys.argv[-1]
        print(f"Accessing file '{file}'")
        return lectura(file)


def opten_good_text(s: str) -> str:
    nex = True
    r = ""
    for i in s:
        if i == "\n" and nex:
            r += "#"
            nex = False
        elif not i == "\n" and not nex:
            nex = True
        r += i
    return r


def writter(s: str) -> None:
    print("Transform data:")
    print("---", end="\n\n")
    r = opten_good_text(s)
    print(r, end="\n\n")
    print("---")
    file = input("Enter new file name (or empty):")
    if file != "":
        writing(file, r)
    else:
        print("Not saving data.")


def writing(file: str, content: str) -> None:
    try:
        fd = open(file, "w")
        print(f"Saving data to '{file}'")
        fd.write(content)
        print(f"Data saved in file '{file}'.")
        fd.close()
    except IOError as e:
        print(f"Error opening file '{file}': {e}")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    x: (str | None) = lectur_file()
    if x is not None:
        writter(x)
