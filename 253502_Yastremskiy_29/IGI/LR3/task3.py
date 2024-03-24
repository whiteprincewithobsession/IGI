def count_digits(input_string: str) -> int:
    """
    Function for counting the number of all digits in a string
    """
    count: int = 0
    for i in range(len(input_string)):
        if input_string[i].isdigit():
            count += 1
    return count