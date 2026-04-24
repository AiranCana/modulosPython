import ex1
from typing import Any, cast
from ex0 import Creature
from ex1.capabilities import HealCapability, TransformCapability


def helin_act(creature: Any) -> None:
    cri = cast(Creature, creature)
    cri2 = cast(HealCapability, creature)
    print(cri.describe())
    print(cri.attack())
    print(cri2.heal())


def trans_act(creature: Any) -> None:
    cri = cast(Creature, creature)
    cri2 = cast(TransformCapability, creature)
    print(cri.describe())
    print(cri.attack())
    print(cri2.transform())
    print(cri.attack())
    print(cri2.revert())


def healig() -> None:
    print("Testing Creature with healing capability\n base:")
    helin_act(ex1.HealingCreatureFactory().create_base())
    print(" evolved:")
    helin_act(ex1.HealingCreatureFactory().create_evolved())


def transorm() -> None:
    print("Testing Creature with transform capability\n base:")
    trans_act(ex1.TransformCreatureFactory().create_base())
    print(" evolved:")
    trans_act(ex1.TransformCreatureFactory().create_evolved())


if __name__ == "__main__":
    healig()
    print()
    transorm()
