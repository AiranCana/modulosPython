def ft_harvest_total():
    day = 1
    i = 0
    while day <= 3:
        i += int(input(f"Day {day} harvest: "))
        day += 1
    print(f"Total harvest: {i}")


if __name__ == "__main__":
    ft_harvest_total()
