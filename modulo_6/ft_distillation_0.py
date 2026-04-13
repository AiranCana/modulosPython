#!/usr/bin/env python3
from alchemy import potions


if __name__ == "__main__":
    print("=== Distillation 0 ===")
    print(f"Testing strength_potion: {potions.strength_potion()}")
    print(f"Testing healing_potion: {potions.healing_potion()}")
