import math

def find_max_number(sequence : list) -> float:
    """
    Function that finds the highest modulo number in the list
    """
    try:
        return max(sequence, key = math.fabs)
    except:
        raise Exception("An item that is not a number is encountered or the list is empty")
    
def find_product_between_zeros(sequence : list) -> float:
    """
    A function that finds the product of all elements enclosed between the first two zeros
    """
    try:
        first_zero_index = sequence.index(0)
        second_zero_index = sequence.index(0, first_zero_index + 1)
    except:
        raise Exception("The required number of null elements is missing")
    product = 1
    for i in range(first_zero_index + 1, second_zero_index):
        product *= sequence[i]
    if first_zero_index == second_zero_index - 1:
        return 0
    return product




