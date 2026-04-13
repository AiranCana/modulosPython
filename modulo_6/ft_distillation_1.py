#!/usr/bin/env python3
from alchemy import strength_potion, healing_potion as heal


if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing heal alias: {heal()}")
