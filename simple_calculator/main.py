NUMBER_OF_ACTIONS = 4
TYPES_OF_DIVISION = ("integer", "normal", "modulus")


def string_to_num(input_data: str) -> int | float:
    try:
        return int(input_data)
    except ValueError:
        try:
            return float(input_data)
        except ValueError:
            raise ValueError(f"Cannot convert '{input_data}' to int or float.")


def custom_sum(a: int | float, b: int | float) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Only numbers are available")

    return a + b


def custom_difference(a: int | float, b: int | float, reversed_diff: bool = False) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Only numbers are available")

    if reversed_diff:
        return b - a
    else:
        return a - b


def custom_product(a: int | float, b: int | float) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Only numbers are available")

    return a * b


def custom_quotient(a: int | float, b: int | float, type_of_division: str = "normal") -> int | float | None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Only numbers are available")

    if b == 0:
        raise ZeroDivisionError("You cannot divide anything by 0.")

    if type_of_division not in TYPES_OF_DIVISION:
        raise TypeError("Incorrect type of division")

    match type_of_division:
        case "integer":
            return a // b
        case "normal":
            return a / b
        case "modulus":
            return a % b
    return None

def main():
    action = int(input("Choose action: \n1. Sum\n2. Subtraction\n3. Multiplication\n4. Division\n"))
    if action not in range(1, NUMBER_OF_ACTIONS + 1):
        raise ValueError("Incorrect action")

    a = string_to_num(input("Choose first number: "))
    b = string_to_num(input("Choose second number: "))

    match action:
        case 1:
            print(custom_sum(a, b))
        case 2:
            reversed_diff = True if input("Do you want to make reversed difference? Y/N").lower() == "y" else False
            print(custom_difference(a, b, reversed_diff))
        case 3:
            print(custom_product(a, b))
        case 4:
            type_of_division = input("Choose the type of division: (integer/normal/modulus)")
            if type_of_division not in TYPES_OF_DIVISION:
                raise ValueError("Incorrect type of division")
            print(custom_quotient(a, b, "integer"))


if __name__ == "__main__":
    main()
