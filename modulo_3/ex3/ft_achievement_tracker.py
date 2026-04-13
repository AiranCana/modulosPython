#!/usr/bin/env python3
import random

ALL_ACHIEVEMENTS = [
    'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme',
    'Untouchable', 'Boss Slayer', 'Strategist', 'Speed Runner', 'Survivor',
    'Treasure Hunter', 'Unstoppable', 'Hidden Path Finder', 'First Steps',
    'Sharp Mind'
]


def gen_player_achievements() -> set[str]:
    lend = random.randint(1, len(ALL_ACHIEVEMENTS))
    return set(random.sample(ALL_ACHIEVEMENTS, lend))


def printPlayers(player: dict[str, set[str]]) -> None:
    for play, ach in player.items():
        print(f"Player {play}: {ach}")


def print_comun_general(player: dict[str, set[str]]) -> None:
    a = player['Alice']
    b = a
    for i, ach in player.items():
        a = a | ach
        b = b & ach
    print(f"\nAll distinct achievements: {a}", end="\n\n")
    print(f"Common achievements: {b}", end="\n\n")


def only_player(player: dict[str, set[str]]) -> None:
    for play, ach in player.items():
        score = set()
        for o_play, o_ach in player.items():
            if o_play != play:
                score |= o_ach
        print(f"Only {play} has: {ach - score}")


def print_missing(player: dict[str, set[str]]) -> None:
    for play, ach in player.items():
        n = set(ALL_ACHIEVEMENTS) - ach
        print(f"{play} is missing: {n}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===", end="\n\n")
    player = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }
    printPlayers(player)
    print_comun_general(player)
    only_player(player)
    print()
    print_missing(player)
