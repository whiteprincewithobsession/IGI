def input_size() -> int:
    """
    A function to check if the sequence size is entered correctly
    """
    size : int = -1
    print("Enter the size of sequence:")
    while(True):
        try:
            size = int(input())
            if(size <= 0):
                raise ValueError
        except ValueError:
            print('Incorrect input, try again! Input only one number greater than zero\n')
            continue
        break
    return size

def choice_checker() -> int:
    """
    Function for checking the choice between 1 and 2 (Input by keyboard or random generator)
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

def int_checker() -> int:
    """
    A function to check if the integer number is entered correctly
    """
    n : int = -1
    print("Enter the number of members of the series:")
    while(True):
        try:
            n = int(input())
            if n <= 0 and n > 500:
                raise ValueError
        except ValueError:
            print('Incorrect input, try again! Input only one integer number in the range (0, 500]\n')
            continue
        break
    return n

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
