#!/usr/bin/env python3
import sys
from typing import IO


def lectura(file: str) -> str | None:
    try:
        fd = open(file, "r")
        sys.stdout.write("---\n\n")
        x = fd.read()
        sys.stdout.write(f"{x}\n\n")
        sys.stdout.write("---\n")
        IO.close(fd)
        sys.stdout.write(f"file {file} closed\n\n")
        sys.stdout.flush()
        return x
    except IOError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file}': {e}")
        return None


def mysplit(s: str, separator: str = '\\') -> list[str]:
    resul = []
    c = ""
    for i in s:
        if i == separator:
            resul += [c]
            c = ""
        else:
            c += i
    resul += [c]
    return resul


def lectur_file() -> (str | None):
    if len(sys.argv) == 1:
        sys.stderr.write("[STDERR] Usage:" +
                         f"{mysplit(sys.argv[0])[-1]} <file>\n")
        return None
    else:
        file = sys.argv[-1]
        sys.stdout.write(f"Accessing file '{file}'\n")
        return lectura(file)


def writter(s: str) -> None:
    sys.stdout.write("Transform data:")
    sys.stdout.write("---\n\n")
    r = opten_good_text(s)
    sys.stdout.write(f"{r}\n\n")
    sys.stdout.write("---\n")
    sys.stdout.flush()
    sys.stdout.write("Enter new file name (or empty):")
    file1 = mysplit(sys.stdin.readline(), '\n')
    file = file1[0]
    if file != "":
        writing(file, r)
    else:
        sys.stdout.write("Not saving data.\n")


def writing(file: str, content: str) -> None:
    try:
        fd = open(file, "w")
        sys.stdout.write(f"Saving data to '{file}'\n")
        fd.write(content)
        sys.stdout.write(f"Data saved in file '{file}'.\n")
        fd.close()
    except IOError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file}': {e}")


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


if __name__ == "__main__":
    sys.stdout = sys.__stdout__
    if sys.stdout is not None:
        sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    x: (str | None) = lectur_file()
    if x is not None:
        writter(x)
