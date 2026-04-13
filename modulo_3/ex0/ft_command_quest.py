#!/usr/bin/env python3
import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name: ft_command_quest.py")
    j = 0
    lis = [i for i in sys.argv[1:]]
    n = 1
    s = len(lis)
    if s != 0:
        print(f"Arguments received: {s}")
        for i in lis:
            print(f"Argument {n}: {i}")
            n += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {s + 1}")
