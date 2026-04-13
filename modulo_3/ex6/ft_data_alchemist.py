#!/usr/bin/env python3
import random

name = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
        "john", "kevin", "Liam"]


def capitalize(lis: list[str]) -> list[str]:
    resul: list[str] = []
    for i in lis:
        if i == i.capitalize():
            resul = resul + [i]
    return resul


def return_score(lis: list[str]) -> dict[str, int]:
    d: dict[str, int] = {}
    for i in lis:
        d.update({i: random.randint(1, 1000)})
    return d


def upper_aveage(dic: dict[str, int], value: float) -> dict[str, int]:
    d: dict[str, int] = {}
    for i in dic:
        if dic[i] >= value:
            d.update({i: dic[i]})
    return d


def average(dic: dict[str, int]) -> float:
    coun = 0
    score = 0
    for i in dic.values():
        score += i
        coun += 1
    value = score / coun
    return value


if __name__ == "__main__":
    print("=== Game Data Alchemist ===", end="\n\n")
    print(f"Initial list of players: {name}")
    allcap = [i.capitalize() for i in name]
    print(f"New list with all names capitalized:{allcap}")
    print(f"New list of capitalized names only: {capitalize(name)}")
    dic = return_score(allcap)
    print(f"Score dict: {dic}")
    value = average(dic)
    print(f"Score average is {value:.2f}")
    uper = upper_aveage(dic, value)
    print(f"High scores: {uper}")
