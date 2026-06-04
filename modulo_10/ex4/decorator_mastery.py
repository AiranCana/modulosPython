#!/usr/bin/env python3
from functools import wraps
from typing import Any
from time import time, sleep
from random import random, randint
from collections.abc import Callable as Call


def spell_timer(func: Call[..., Any]) -> Call[..., Any]:
    @wraps(func)
    def wrapser(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time()
        sleep(random() * randint(1, 3))
        result = func(*args, **kwargs)
        end = time()
        times = end - start
        print(f"Spell completed in {times:.3f} seconds")
        return result
    return wrapser


def power_validator(min_power: int) -> Call[..., Any]:
    def validator(func: Call[..., Any]) -> Call[..., Any]:
        @wraps(func)
        def wrapser(*args: Any, **kwargs: Any) -> Any:
            for n in args:
                if isinstance(n, int):
                    i = n
                    break
            if i < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapser
    return validator


def retry_spell(max_attempts: int) -> Call[..., Any]:
    counter = 0

    def retry(func: Call[..., Any]) -> Call[..., Any]:
        @wraps(func)
        def wrapser(*args: Any, **kwargs: Any) -> Any:
            nonlocal counter
            if counter == max_attempts:
                return f"Spell casting failed after {max_attempts} attempts"
            else:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    counter += 1
                    if counter != max_attempts:
                        return ("Spell failed, retrying... (attempt "
                                f"{counter}/{max_attempts})")
                    else:
                        return (f"Spell casting failed after {max_attempts}"
                                " attempts")
        return wrapser
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            if name.replace(" ", "").isalpha():
                return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with <{power}> power"


@retry_spell(3)
def firball(power: int) -> str:
    if power % 2 == 0:
        return f"I cast fireball ({power} power)"
    raise Exception("")


@spell_timer
def ice(power: int) -> str:
    return f"I cast ice ({power} power)"


if __name__ == "__main__":
    mague = MageGuild()
    print("Testing spell timer...")
    print(ice(50))
    print("\nTesting retrying spell...")
    print(firball(13))
    print(firball(12))
    print(firball(13))
    print(firball(13))
    print(mague.cast_spell("fireball", 9))
    print(MageGuild.validate_mage_name("hola"))
