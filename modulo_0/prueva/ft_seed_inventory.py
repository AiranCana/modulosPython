def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit in ("packets", "area", "grams"):
        print(f"{seed_type} seeds: ", end="")
        if unit == "packets":
            print(f"{quantity} {unit} available")
        elif unit == "area":
            print(f"{quantity} {unit} total")
        else:
            print(f"covers {quantity} square meters")
    else:
        print("Unknown unit type")


if __name__ == "__main__":
    ft_seed_inventory("tomato", 8, "area")
