import random
import string

def float_sequence(size : int) -> list:
    """
    Function for generating float sequence of arbitrary size
    Numbers are generated in the interval [-10, 10] with 2 decimal places
    """
    sequence : list = []
    for i in range(size):
        sequence.append(float(format(random.uniform(-10, 10), '.2f')))
    pos1 = random.randint(0, len(sequence) - 1)
    sequence[pos1] = 0
    pos2 = pos1
    while pos2 == pos1:
        pos2 = random.randint(0, len(sequence) - 1)
        sequence[pos2] = 0
    return sequence


def literal_sequence(size : int) -> str:
    """
    Function for generating string of arbitrary size
    Using all printable ASCII characters
    """
    random_string = ''.join(random.choices(string.printable, k=size))
    return random_string

def int_sequence(size : int) -> list:
    """
    Function for generating int sequence of arbitrary size
    Numbers are generated in the interval [-10, 150]
    """
    sequence : list = []
    for i in range(size):
        sequence.append(random.randint(-10, 150))
    return sequence
     
