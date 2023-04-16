from typing import List, Union, Tuple, Dict

# Global variables
default_denominations = [500.00, 200.00, 100.00, 50.00, 20.00, 10.00,
                 5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]


def anyToFloat(*args: Union[str, int, float]) -> List[float]:
    # Create an empty list to store the final float list.
    float_list: List[float] = []
    
    # Iterate through the `args` arguments using a for loop.
    for arg in args:
        # Check if the argument is of type `int` or `float`. If so, convert it to a `float` and add it to the `float_list` list.
        if isinstance(arg, (int, float)):
            float_list.append(float(arg))
        # If the argument is of type `str`, try to replace comma (',') with a dot ('.') using the `replace()` method. Then convert the string to a `float` and add it to the `float_list` list. If this is not possible (e.g. when the string does not represent a number), skip the argument.
        elif isinstance(arg, str):
            try:
                float_list.append(float(arg.replace(',', '.')))
            except ValueError:
                pass
    
    # Remove duplicates from the `float_list` list using the `set()` function and convert it back to a list.
    float_list = list(set(float_list))
    
    # Sort the `float_list` list in descending order (from largest to smallest) using the `sort()` method with the `reverse=True` argument.
    float_list.sort(reverse=True)
    
    # Round each number in the `float_list` list to 2 decimal places using the `round()` function.
    float_list = [round(float_num, 2) for float_num in float_list]
    
    # Return the `float_list` list.
    return float_list


def userInput() -> Tuple[str, List[float]]:
    # Get user input as a string
    user_input: str = input(">")

    # Split the user input into a list of words
    input_list: List[str] = user_input.split()

    # Extract the command and args from the input list
    command: str = input_list[0]
    args: List[str] = input_list[1:]

    # Convert arguments to float using the helper function 'anyToFloat'
    args: List[float] = anyToFloat(*args)

    # Return the command and args as a tuple of strings and floats
    return command, args


def removeDenominations(denominations: List[float], *args: float) -> List[float]:
    # Create a new list that will store the denominations that won't be removed
    new_denominations = denominations.copy()
    
    # Iterate through all arguments passed to the function, which have been converted to a list of floats
    for arg in args:
        # Iterate through all denominations in the list and remove denominations that are equal to the passed argument
        for denomination in denominations:
            if denomination == arg:
                new_denominations.remove(denomination)
    
    return new_denominations



def addDenominations(denominations: List[float], *args: List[float], default_denominations: List[float] = []) -> List[float]:
    # Create a new list to store denominations that will be added
    added_denominations: List[float] = []

    # Iterate over all arguments passed to the function
    for arg in args:
        # Check if the denomination is in the default list
        if arg in default_denominations:
            # Add the new denomination to the added denominations list
            added_denominations.append(arg)

    # Add the new denominations to the denominations list
    denominations += added_denominations

    # Remove duplicate denominations and sort the list from the largest to the smallest denomination
    denominations = sorted(list(set(denominations)), reverse=True)

    return denominations


def displayChangeResults(denominations: List[float], args: List[float]) -> None:
    def Change(denominations: List[float], args: float) -> dict:
        # Sort denominations in descending order
        denominations.sort(reverse=True)

        # Calculate the total amount of change required
        total_change = round(args, 2)

        # Create an empty dictionary to store the count of each denomination
        change_dict = {}

        # Loop through each denomination
        for denom in denominations:
            # Check if the denomination can be used to give change
            if total_change >= denom:
                # Calculate the number of coins/bills needed for this denomination
                count = int(total_change // denom)

                # Reduce the total change by the amount given in this denomination
                total_change -= denom * count

                # Store the count of this denomination in the dictionary
                change_dict[denom] = count

        # Return the dictionary containing the count of each denomination used to give change
        return change_dict
    
    # Iterate over each argument in *args
    for arg in args:
        # Call the Change function to calculate the change for the current argument
        change_dict = Change(denominations, arg)

        # Print the result for the current argument
        print(f"For {arg} change, you need:")

        # Iterate over the change dictionary and print the count of each denomination
        for denom, count in change_dict.items():
            print(f"{count} x {denom}")

def help():
    print("Here are the available commands:")
    print("exit - quits the program")
    print("add [denomination_1] [denomination_2] ... - adds given denominations to the list of available denominations")
    print("remove [denomination_1] [denomination_2] ... - removes the given denomination from the list of available denominations")
    print("change [amount_1] [amount_2] ... - calculates the given changes for the specified amounts")
    print("list - displays the current list of denominations")
    print("help - displays this help message")


def main() -> int:
    denominations = [500.00, 200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

    print("Use help for more info")
    while True:
        command, args = userInput()

        if command == "exit":
            return 0
        
        if command == "add":
            denominations = addDenominations(denominations, *args)

        if command == "remove":
            denominations = removeDenominations(denominations, *args)

        if command == "change":
            displayChangeResults(denominations, args)
        
        if command == "list":
            print(denominations)

        if command == "help":
            help()


main()
