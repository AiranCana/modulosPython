#!/usr/bin/env python3
from typing import Callable as Call
import random


def spell_combiner(spell1: Call[[str, int], str],
                   spell2: Call[[str, int], str]) -> Call[
                       [list[str], list[int]], str]:
    def fusion(targets: list[str], powers: list[int]) -> str:
        result1 = spell1(targets[0], powers[0])
        result2 = spell2(targets[1], powers[1])
        return f"{result1}, {result2}"
    return fusion


def power_amplifier(base_spell: Call[[], int]) -> Call[[int], int]:
    def amplifer(multiplier: int) -> int:
        return (multiplier * base_spell())
    return amplifer


def conditional_caster(condition: Call[..., bool],
                       spell: Call[..., str]) -> Call[..., str]:
    def conditions(number: int, targ: str, power: int | list[int],
                   i: int = -1) -> str:
        if condition(number, i):
            return spell(targ, power)
        return "Spell fizzled"
    return conditions


def spell_sequence(spells: list[Call[..., str]]) -> Call[
                   [str, list[int]], str]:
    def sequence(target: str, power: list[int]) -> str:
        sol = ""
        n = 0
        for i in spells:
            sol = " ".join([sol, i(target, power[n])])
            n += 1
        return sol
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball engulfs {target} in flames for {power} damage"


def ice_lance(target: str, power: int) -> str:
    return f"Ice Lance pierces {target} for {power} frost damage"


def lightning_bolt(target: str, power: int) -> str:
    return f"Lightning Bolt strikes {target} for {power} electric damage"


def shadow_curse(target: str, power: int) -> str:
    return f"Shadow Curse weakens {target} reducing power by {power}"


def comprobation_funtions(i: int, lists: int) -> bool:
    if lists == -1:
        return (i % 2) == 0
    return i == lists


def power() -> int:
    return random.randint(1, 6)


if __name__ == "__main__":
    lis = [fireball, ice_lance, lightning_bolt, shadow_curse]
    powe = []
    for _ in range(len(lis)):
        powe += [power() * 15]
    sequence = spell_sequence(lis)
    condition1 = conditional_caster(comprobation_funtions, sequence)
    print(condition1(len(powe), "Sultan", powe, len(lis)))
    ampliate = power_amplifier(power)
    print(fireball("Merlin", ampliate(20)))
    combinate = spell_combiner(fireball, ice_lance)
    print(combinate(["Hugabuga", "Merlin"], [ampliate(20), ampliate(15)]))
    print(combinate(["Pablo", "Airan"], [ampliate(20), ampliate(15)]))
