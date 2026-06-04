#!/usr/bin/env python3
from typing import Any
from collections.abc import Callable as Call


def mage_counter() -> Call[..., int]:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Call[[int], int]:
    summ: int = initial_power

    def accumulator(number: int) -> int:
        nonlocal summ
        summ += number
        return summ
    return accumulator


def enchantment_factory(enchantment_type: str) -> Call[[str], str]:
    enchante: str = enchantment_type

    def enchantment(object: str) -> str:
        nonlocal enchante
        enchante += f" {object}"
        return enchante
    return enchantment


def memory_vault() -> dict[str, Call[..., Any]]:
    objects: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        objects.update({key: value})

    def recall(key: str) -> Any:
        return objects.get(key, "Memory not found")
    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    count_a = mage_counter()
    count_b = mage_counter()
    for n in range(10):
        print(f"count_a {n}: {count_a()}")
        if n == 5:
            count_a = mage_counter()
    print(f"count_b 1: {count_b()}")

    print("\nTesting spell accumulator...")
    base = 100
    acumulate = spell_accumulator(base)
    print(f"Base {base}, add 20: {acumulate(20)}")
    print(f"Base {base}, add 30: {acumulate(30)}")

    print("\nTesting enchantment factory...")
    flam = enchantment_factory("Flameling")
    froz = enchantment_factory("Frozen")
    print(flam("Sword"))
    print(flam("Shield"))
    print(froz("Sword"))
    print(froz("Shield"))

    print("\nTesting memory vault...")
    memory = memory_vault()
    print("Store 'secret' = 42")
    memory["store"]("secret", 42)
    print(f"Recall 'secret': {memory['recall']('secret')}")
    print(f"Recall 'unknown': {memory['recall']('unknown')}")
