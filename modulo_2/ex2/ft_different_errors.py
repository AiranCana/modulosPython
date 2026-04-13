#!/usr/bin/env python3
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        5/0
    if operation_number == 2:
        open("./error.txt")
    if operation_number == 3:
        "hola" + 5


def test_error_types() -> None:
    itere = [0, 1, 2, 3, 4]
    print("=== Garden Error Types Demo ===")
    for i in itere:
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
