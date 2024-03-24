import string

task_string = 'So she was considering in her own mind, as well as she could, for the hot day made \
her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be \
worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.'

def transform_string(input_string: str) -> None:
    """
    A function that converts a string to replace all non-letter characters with spaces
    """
    i = 0
    temp_str = list(input_string)
    while i < len(temp_str):
        if temp_str[i] not in string.ascii_letters and temp_str[i] != '-':
            temp_str[i] = ' '
        i += 1
    return  "".join(temp_str)

def count_words(input_string: str) -> int:
    """
    A function that counts the number of words in a line that does not exceed 7
    """
    ls = input_string.split()
    count = 0
    for i in range(len(ls)):
        if(len(ls[i]) < 7):
            count += 1
    return count
    
def words_in_descending_order(input_string: str) -> list[str]:
    """
    A function that displays a list of words from a string in descending order of length
    """
    ls = input_string.split()
    ls.sort(key=len, reverse = True)
    return ls

def find_minimal_word(input_string: str) -> str:
    """
    A function that finds a word of minimum length ending in the letter 'a'
    """
    ls = input_string.split()
    ls.sort(key=len, reverse=True)
    for i in range(len(ls)):
        if ls[i][-1] == 'a':
            return ls[i]
        
    