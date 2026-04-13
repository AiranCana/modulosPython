#!/usr/bin/env python3
import alchemy

if __name__ == "__main__":
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("""Now show that not all functions can be reached
This will raise an exception!""")
    print(alchemy.create_earth())
