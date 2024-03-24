def input_numbers() -> list[int]:
    """
    Enters numbers until stop number 133 is entered
    """
    sequence : list[int] = []
    a = 0
    while(a != 133):
        try:
            print("Enter the number (description: enter the 133 to stop): ")
            a = int(input())
            sequence.append(a)
        except ValueError:
            print('Incorrect input, try again! Input only one number\n')
            continue
        
    return sequence

def count_numbers(sequence : list) -> int:
    """
    Counts all numbers greater than 12 in the sequence
    """
    count : int = 0
    i : int = 0
    try:
        if sequence[0] == 133:
            return 1
        while sequence[i] != 133:
            if sequence[i] > 12:
                count += 1
            i += 1
    except:
        raise Exception("ERROR: 133 not founded")
    return count + 1


    