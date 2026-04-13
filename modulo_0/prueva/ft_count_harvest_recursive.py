def recursive(i, d=1):
    print(f"Day {d}")
    if i != d:
        recursive(i, d+1)


def ft_count_harvest_recursive():
    i = int(input("Days until harvest: "))
    recursive(i)
    print("Harvest time!")


if __name__ == "__main__":
    ft_count_harvest_recursive()
