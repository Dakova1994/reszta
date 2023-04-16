from typing import List, Union, Tuple, Dict

AVAILABLE_DENOMINATIONS = [500.00, 200.00, 100.00, 50.00, 20.00, 10.00,
                           5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]


# TODO:

def main() -> int:
    denominations = [500.00, 200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

    print("Use help for more info")
    while True:
        command, args = user_input()

        if command == "exit":
            return 0
        elif command == "add":
            denominations = add_denominations(denominations, *args, AVAILABLE_DENOMINATIONS)
        elif command == "remove":
            denominations = remove_denominations(denominations, *args)
        elif command == "change":
            display_change_results(denominations, args)
        elif command == "list":
            print(denominations)
        else:
            help()


# converting string to float exception handling
def string_to_float(*args: List[str]) -> List[float]:
    float_list: List[float] = []
    for arg in args:
        try:
            float_list.append(float(arg.replace(',', '.')))
        except ValueError:
            print("Only numbers as arguments")
    return float_list


def user_input() -> Tuple[str, List[float]]:
    user_input: str = input(">")
    input_list: List[str] = user_input.split()
    command: str = input_list[0]
    args: List[str] = input_list[1:]
    args: List[float] = string_to_float(*args)
    return command, args


def remove_denominations(denominations: List[float], *args: float) -> List[float]:
    for arg in args:
        for denomination in denominations:
            if denomination == arg:
                denominations.remove(arg)
    return denominations


def add_denominations(denominations: List[float], *args: List[float], default_denominations: List[float] = []) -> List[
    float]:
    for arg in args:
        if (arg in default_denominations) and (arg not in denominations):
            denominations.append(arg)
    return sorted(denominations, reverse=True)


def display_change_results(denominations: List[float], args: List[float]) -> None:
    def has_only_two_decimal_places(num: float) -> bool:
        return len(str(num).split('.')[1]) <= 2

    def round_to_two_decimal(arg: float) -> float:
        rounded_arg = round(arg, 2)
        print(f"Warning: Your input {arg} has been rounded to MIN two decimal places: {rounded_arg}.")
        return rounded_arg

    def calculate_change(denominations: List[float], total_change: float) -> dict:
        change_dict = {}
        for denom in denominations:
            if total_change >= denom:
                count = int(total_change // denom)
                total_change -= denom * count
                change_dict[denom] = count
        return change_dict

    for arg in args:
        if has_only_two_decimal_places(arg):
            arg = round_to_two_decimal(arg)
        change_dict = calculate_change(denominations, arg)
        print(f"For {arg} change, you need:")
        for denom, count in change_dict.items():
            print(f"{count} x {denom}")


def help() -> None:
    print(f'''Usage: COMMAND [ARGUMENTS ...]
    )
    Available commands:
    exit                - Quits the program.
    add  DENOMINATIONS  - Adds given denominations to the list of available denominations.
                           DENOMINATIONS should be a list of numbers separated by space.
    remove DENOMINATIONS - Removes the given denominations from the list of available denominations.
                           DENOMINATIONS should be a list of numbers separated by space.
    change AMOUNTS      - Calculates the change for the specified amounts.
                           AMOUNTS should be a list of numbers separated by space.
    list                - Displays the current list of denominations.
    help                - Displays this help message.
    )
    Default denominations are: , {AVAILABLE_DENOMINATIONS})
    )
    Note: Decimal points should be represented using a period '.' and not a comma ','.
          Only the first two decimal places are taken into account.
          If the input amount has more than two decimal places, it will be rounded to two decimal places.
    )
    Examples:
      add 0.02 0.01        - Adds 0.02 and 0.01 to the list of denominations.
      remove 0.50 0.20     - Removes 0.50 and 0.20 from the list of denominations.
      change 10.50 1.75    - Calculates the change for 10.50 and 1.75.
''')



if __name__ == '__main__':
    main()