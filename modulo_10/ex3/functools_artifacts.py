#!/usr/bin/env python3
from typing import Any
from typing import Callable as Call
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    try:
        if len(spells) == 0:
            return 0
        ops = {
            "add": operator.add,
            "multiply": operator.mul,
            "max": lambda a, b: a if operator.gt(a, b) else b,
            "min": lambda a, b: a if operator.lt(a, b) else b
        }
        return reduce(ops[operation], spells)
    except Exception:
        raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(base_enchantment: Call[..., Any]
                      ) -> dict[str, Call[..., Any]]:
    return {
        "fire": partial(base_enchantment, 100, "fireball"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 80, "lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Call[[Any], str]:
    @singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher


def spell(power: int, tipe: str, target: str) -> str:
    return f"{target} cast {tipe} ({power} power)"


if __name__ == "__main__":
    print("Testing spell reducer...")
    lists = [45, 13, 9, 20, 36, 3, 8, 76, 48, 756, 62, 548, 134]
    oper = ["add", "multiply", "max", "min", "Hello"]
    for i in oper:
        try:
            result = spell_reducer(lists, i)
            print(f"{i}: {result}")
        except ValueError as e:
            print(e)
    print("\nTesting memoized fibonacci...")
    for n in range(5):
        print(memoized_fibonacci(lists[n]))
    dic = partial_enchanter(spell)
    print("\nTesting partial enchanter...")
    print(dic["fire"]("Merlin"))
    print(dic["ice"]("Merlin"))
    print(dic["lightning"]("Merlin"))
    print("\nTesting spell dispatcher...")
    more_spell = spell_dispatcher()
    print(more_spell(12))
    print(more_spell("fire"))
    print(more_spell(lists))
    print(more_spell({10: "fire"}))
