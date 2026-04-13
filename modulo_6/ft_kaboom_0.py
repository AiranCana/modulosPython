#!/usr/bin/env python3
from alchemy import grimoire


if __name__ == "__main__":
    print("""=== Kaboom 0 ===
Using grimoire module directly
Testing record light spell:""", end="")
    print(grimoire.light_spell_record("Fantasy", "Earth, wind and fire"))
