#!/usr/bin/env python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda ar: ar["power"], reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    transformer = map(lambda spe: "* " + spe + " *", spells)
    return [i for i in transformer]


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    ma = max(mages, key=lambda ar: ar["power"])["power"]
    mi = min(mages, key=lambda ar: ar["power"])["power"]
    avg = sum(map(lambda x: x["power"], mages))/len(mages)
    result = {}
    result.update({"max_power": ma, "min_power": mi, "avg_power": avg})
    return result


def print_mages(itera: list[dict[str, Any]]) -> None:
    for i in itera:
        print(
            f" - {i['name']} ({i['power']} power) "
            f"element: {i['element']}", end=" "
        )


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 93, 'type': 'focus'},
        {'name': 'Wind Cloak', 'power': 99, 'type': 'focus'},
        {'name': 'Crystal Orb', 'power': 120, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 76, 'type': 'focus'}
    ]
    mages = [
        {'name': 'Ash', 'power': 81, 'element': 'ice'},
        {'name': 'Sage', 'power': 66, 'element': 'fire'},
        {'name': 'Nova', 'power': 76, 'element': 'lightning'},
        {'name': 'Alex', 'power': 87, 'element': 'fire'},
        {'name': 'Kai', 'power': 63, 'element': 'water'}
    ]
    spells = ['tornado', 'earthquake', 'flash', 'freeze']
    print("\nTesting artifact sorter...")
    for i in artifact_sorter(artifacts):
        print(
            f" - {i['name']} ({i['power']} power) "
            f"type: {i['type']}", end=" "
        )
    num = 70
    print(f"\n\nTesting power filter... ({num})")
    print_mages(power_filter(mages, num))
    print("\n\nTesting spell transformer...")
    for i in spell_transformer(spells):
        print(f"{i} ", end="")
    print(end="\n\n")
    itera = mage_stats(mages)
    print("Testing mage stats...\nIn: ")
    print_mages(mages)
    print(
        f"\nthere are a max power: {itera['max_power']}, "
        f"min power: {itera['min_power']} and "
        f"average power: {itera['avg_power']}"
    )
