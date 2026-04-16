from ex0 import AquaFactory, FlameFactory, Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from ex2 import DefensiveStrategy, AggressiveStrategy, NormalStrategy
from ex2 import BattleStrategy
from typing import Any


def combat(first: tuple[Creature, BattleStrategy],
           second: tuple[Creature, BattleStrategy]) -> None:
    cri1 = first[0]
    stra1 = first[1]
    cri2 = second[0]
    stra2 = second[1]
    print(stra1.act(cri1))
    print(stra2.act(cri2), end="\n\n")


def battle(first: tuple[Creature, BattleStrategy],
           second: tuple[Creature, BattleStrategy],
           verifi: bool = False) -> None:
    cri1 = first[0]
    stra1 = first[1]
    cri2 = second[0]
    stra2 = second[1]
    try:
        print("* Battle *")
        print(cri1.describe())
        print(" vs.")
        print(cri2.describe())
        print(" now fight!")
        if verifi:
            if stra1.is_valid(cri1) and stra2.is_valid(cri2):
                combat(first, second)
            else:
                print("No Strategy compatible", end="\n\n")
            return
        combat(first, second)
    except TypeError as e:
        print(f"Battle error, aborting tournament: {e}", end="\n\n")


def print_strat(strat: BattleStrategy) -> None:
    if isinstance(strat, DefensiveStrategy):
        print("Defensive", end="")
    elif isinstance(strat, AggressiveStrategy):
        print("Aggressive", end="")
    else:
        print("Normal", end="")


def print_name(name: Any) -> None:
    if isinstance(name, HealCapability):
        print("Healing+", end="")
    elif isinstance(name, TransformCapability):
        print("Transform+", end="")
    else:
        print(f"{name._name}+", end="")


def print_nam_stra(strat: BattleStrategy, name: Any) -> None:
    print_name(name)
    print_strat(strat)


def print_combatients(lis: list[tuple[BattleStrategy, Any]]) -> None:
    final = len(lis) - 1
    n = 0
    print("[ ", end="")
    for i, j in lis:
        print("(", end="")
        print_nam_stra(i, j)
        print(")", end="")
        if n != final:
            print(", ", end="")
        n += 1
    print(" ]")
    print("*** Tournament ***")


if __name__ == "__main__":
    defe = DefensiveStrategy()
    agr = AggressiveStrategy()
    nor = NormalStrategy()
    flam = FlameFactory().create_base()
    aqu = AquaFactory().create_base()
    trans = TransformCreatureFactory().create_base()
    hel = HealingCreatureFactory().create_base()
    print("Tournament 0 (basic)")
    print_combatients([(nor, flam), (defe, hel)])
    print("*** Tournament ***")
    print("2 opponents involved", end="\n\n")
    battle((flam, nor), (hel, defe))
    print("Tournament 1 (error)")
    print_combatients([(agr, flam), (defe, hel)])
    print("2 opponents involved", end="\n\n")
    battle((flam, agr), (hel, defe))
    print("Tournament 2 (multiple)")
    print_combatients([(nor, aqu), (defe, hel), (agr, trans)])
    print("3 opponents involved", end="\n\n")
    battle((aqu, nor), (hel, defe))
    battle((aqu, nor), (trans, agr))
    battle((hel, defe), (trans, agr))
