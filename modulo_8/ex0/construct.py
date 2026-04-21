#!usr/bin/env python3
import sys
import os
import site


def main() -> None:
    print()
    print("MATRIX STATUS: ", end="")
    en_vir = sys.prefix != sys.base_prefix
    if en_vir:
        print("Welcome to the construct", end="\n\n")
    else:
        print("You're still plugged in", end="\n\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: ", end="")
    if en_vir:
        enviro = os.environ.get("VIRTUAL_ENV")
        print(f"Environment Path: {enviro}", end="\n\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.", end="\n\n")
        print("Package installation path:")
        print(site.getsitepackages()[0])
    else:
        print("None detected", end="\n\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.", end="\n\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows", end="\n\n")

        print("Then run this program again.")


if __name__ == "__main__":
    main()
