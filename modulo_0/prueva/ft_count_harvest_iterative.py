def ft_count_harvest_iterative():
    i = int(input("Days until harvest: "))
    for n in range(1, i+1):
        print(f"Day {n}")
    print("Harvest time!")


if __name__ == "__main__":
    ft_count_harvest_iterative()
