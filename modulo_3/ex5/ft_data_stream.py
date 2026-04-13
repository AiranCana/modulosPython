#!/usr/bin/env python3
from typing import Generator
import random

actions = ["run", "eat", "sleep", "grab", "move", "climb",
           "swim", "release", "use"]
players = ["bob", "alice", "dylan", "charlie"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield name, action


def consume_event(lis: list[tuple[str, str]]) -> Generator[tuple[str, str],
                                                           None, None]:
    while True:
        yield lis.pop(random.randint(0, len(lis) - 1))
        print(f"Remains in list: {lis}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")
    lis = [next(gen) for _ in range(10)]
    event = consume_event(lis)
    print(f"Built list of 10 events: {lis}")
    for _ in range(10):
        print(f"Got event from list: {next(event)}")
    print(f"Remains in list: {lis}")
