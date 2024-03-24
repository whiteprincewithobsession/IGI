from launch_tasks import start_task1, start_task2, start_task3, start_task4, start_task5
from checkers import choice_checker

#Lab3. Standard data types, collections, functions, modules.
#Performed by a student of group 253502, Yastremsky Yaroslav.
#Fulfillment date: 20.03.2024

def main():
    task : int = -1
    while(True):
        print("Enter the number of task from 1 to 5, or 6 to exit:")
        try:
            task = int(input())
            if task <= 0 or task > 6:
                raise Exception
        except:
            print('Incorrect input, try again! Input only one number between 1 and 5, or 6 to exit\n')
            continue
        if task == 1:
            print('''Task #1.\nCompose a program to compute the value of a function by factoring the function into a power series.
Set the precision of eps calculations.''')
            start_task1(choice_checker())
        elif task == 2:
            print("Task #2.\nOrganize a loop that takes integers and calculates the number of numbers greater than 12. End of Cycle – Input 133\n")
            start_task2(choice_checker())
        elif task == 3:
            print("Task #3.\nIn the string entered from the keyboard, count the number of digits.\n")
            start_task3(choice_checker())
        elif task == 4:
            print('''Task #4.\nA line of text is given in which the words are separated by spaces and commas.
In accordance with the task of your version, write a program to analyze the string initialized in the program code:\n
a) determine the number of words that are less than 7 characters long;\n
b) find the shortest word ending in the letter 'a';\n
c) display all words in descending order of their lengths\n''')
            start_task4()
        elif task == 5:
            print('''Task #5.\nCompile a program for processing float lists.\n
Find the number of the maximum modulo item in the list.\n
Find the product of the elements between the first and second null elements\n
                  ''')
            start_task5(choice_checker())
        elif task == 6:
            return
            


if __name__ == '__main__':
    main()