def input_size(param : str, left : int) -> int:
    """
    A function to check if the int parameter is entered correctly.
    """
    size : int = -1
    print(f"Enter the value of {param}:")
    while(True):
        try:
            size = int(input())
            if(size <= left):
                raise ValueError
        except ValueError:
            print(f'Incorrect input, try again! Input only one number greater than {left}\n')
            continue
        break
    return size

def choice_checker() -> int:
    """
    Function for checking the choice between 1 and 2 (Input by keyboard or random generator).
    """
    while(True):
        print("Enter your choice:\n1 - Enter it yourself\n2 - Random generator\n")
        try:
            choice = int(input())
            if choice != 1 and choice != 2:
                raise ValueError
        except ValueError:
            print('Incorrect input, try again! Input only one number\n1 - Enter it yourself\n2 - Random generator\n')
            continue
        break
    return choice

def float_checker(a : float, b : float) -> float:
    """
    A function to check if the float number in the range is entered correctly
    """
    number : float = 0.0
    while(True):
        print(f'Enter float number in the range ({a}, {b}):')
        try:
            number = float(input())
            if number < a or number >= b:
                raise ValueError
        except ValueError:
            print('Incorrect input, try again!\n')
            continue
        break
    return number
