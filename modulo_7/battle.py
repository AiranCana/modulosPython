import ex0


def test_factory(factory: ex0.CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print("Testing factory")
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle() -> None:
    c1 = ex0.AquaFactory().create_base()
    c2 = ex0.FlameFactory().create_base()
    print("Testing battle")
    print(c1.describe())
    print(" vs.")
    print(c2.describe())
    print(" fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    test_factory(ex0.FlameFactory())
    test_factory(ex0.AquaFactory())
    battle()
