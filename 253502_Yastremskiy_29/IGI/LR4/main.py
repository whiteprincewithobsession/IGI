from task1.launch_task1 import start_task1
from task2.launch_task2 import start_task2
from task3.launch_task3 import start_task3
from task4.launch_task4 import start_task4
from task5.launch_task5 import start_task5

#Lab4. Work with files, classes, serializers, regular expressions, and standard libraries.  
#Performed by a student of group 253502, Yastremskiy Yaroslav.
#Fulfillment date: 07.04.2024.

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
            print('''Task #1.\nThe source data is a dictionary. You need to put them in a file using a serializer.
Organize data reading, search, sorting in accordance with an individual task. Be sure to use classes.
Implement two options: 1)CSV file format; 2)Pickle module''')
            start_task1()
        elif task == 2:
            print('''Task #2.\nIn accordance with the task of your version, create a program for text analysis.
Read text from the source file. Using regular expressions, get the information you are looking for (see the condition),
display it on the screen and save it to another file.
Archive the file with the result using the zipfile module and provide information about the file in the archive.
Also perform a general task – define and save to a file with results\n\n''')
            start_task2()
        elif task == 3:
            print('''Task #3.\nIn accordance with the task of your version, modify the program from LR3 by using the class and provide:
a) determination of additional parameters: arithmetic mean of the sequence elements, median, mode, variance, RMS of the sequence;
b) Using the matplotlib library, draw graphs of different colors in the same coordinate axis:''')
            start_task3()
        elif task == 4:
            print('''Task #4.\nDraw a regular n-gon with side a.''')
            start_task4()
        elif task == 5:
            print('''Task #5.Calculate the sum of the matrix elements below the main diagonal. 
Calculate Standard Deviation for Main Diagonal Elements
Matrix. Round the answer to the nearest hundredth. Calculating the standard deviation
In two ways: through the standard function and through the Formula Programming''')
            start_task5()
        elif task == 6:
            return
            
            
if __name__ == '__main__':
    main()