#!/usr/bin/env python3
from typing import Callable


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]) -> Callable[
                       [list[str], list[int]], str]:
    def fusion(targets: list[str], powers: list[int]) -> str:
        result1 = spell1(targets[0], powers[0])
        result2 = spell2(targets[1], powers[1])
        return f"{result1}, {result2}"
    return fusion


def power_amplifier(base_spell: Callable[[None], int],
                    multiplier: int) -> Callable[[None], int]:
    def amplifer() -> int:
        return multiplier * base_spell()
    return amplifer


def conditional_caster(condition: Callable[[...], bool],
                       spell: Callable[[str, int], str]) -> Callable[
                           [int, str, int], str]:
    def conditions(number: int, targ: str, power: int) -> str:
        if condition(number):
            return spell(targ, power)
        return "Spell fizzled"
    return conditions


def spell_sequence(spells: list[Callable[[...], str]]) -> Callable[
                   [str, list[int]], str]:
    def sequence(target: str, power: list[int]) -> str:
        sol = ""
        n = 0
        for i in spells:
            sol.join(i(target, power[n]))
            n += 1
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball engulfs {target} in flames for {power} damage"


def ice_lance(target: str, power: int) -> str:
    return f"Ice Lance pierces {target} for {power} frost damage"


def lightning_bolt(target: str, power: int) -> str:
    return f"Lightning Bolt strikes {target} for {power} electric damage"


def shadow_curse(target: str, power: int) -> str:
    return f"Shadow Curse weakens {target} reducing power by {power}"


def 