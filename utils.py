

# converting string to float exception handling
from typing import List


def string_to_float(*args: List[str]) -> List[float]:
    float_list: List[float] = []
    for arg in args:
        try:
            float_list.append(float(arg.replace(',', '.')))
        except ValueError:
            print("Only numbers as arguments")
    return float_list


def has_only_two_decimal_places(num: float) -> bool:
    return len(str(num).split('.')[1]) <= 2


def round_to_two_decimal(arg: float) -> float:
    rounded_arg = round(arg, 2)
    print(f"Warning: Your input {arg} has been rounded to MIN two decimal places: {rounded_arg}.")
    return rounded_arg