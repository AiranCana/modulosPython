#!/usr/bin/env python3
import sys


def generate() -> None | list[int]:
    allgood = True
    for i in sys.argv[1:]:
        try:
            int(i)
        except ValueError:
            allgood = False
            print(f"Invalid parameter: '{i}'")
    if not allgood:
        return None
    return [int(i) for i in sys.argv[1:]]


def printable() -> None:
    print("=== Player Score Analytics ===")
    lis = generate()
    if not lis:
        print("No scores provided. Usage: python3 ft_score_analytics.py" +
              " <score1> <score2> ...")
        return
    total = len(lis)
    print(f"Total players: {total}")
    score = sum(lis)
    print(f"Total score: {score}")
    print(f"Average score: {(score/total):.1f}")
    maxi = max(lis)
    mini = min(lis)
    print(f"High score: {maxi}")
    print(f"Low score: {mini}")
    print(f"Score range: {maxi - mini}")


if __name__ == "__main__":
    printable()
