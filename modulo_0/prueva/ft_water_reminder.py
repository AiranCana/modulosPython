def ft_water_reminder():
    i = int(input("Days since last watering: "))
    if i > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


if __name__ == "__main__":
    ft_water_reminder()
