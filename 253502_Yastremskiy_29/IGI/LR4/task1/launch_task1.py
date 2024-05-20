from task1.student import Student
from task1.serializers import Serializers
import pickle
from utils.checkers import input_size

students = {
    '1':Student("Petrashko M.O.", 12, 5, 2001, 4),
    '2':Student("Aijrgo F.A.", 1, 3, 2005, 1),
    '3':Student("Ijearoga M.Y.", 2, 12, 2012, 2),
    '4':Student("Salfakgvam H.I.", 3, 5, 2008, 3)
}

def start_task1():
    Serializers.serialize_to_csv(students, 'students.csv')
    Serializers.serialize_to_pickle(students, 'students.pkl')

    month = input_size("Month", 1)
    
    print("Info from *.pkl file:\n")
    with open('students.pkl', 'rb') as picklefile:
        l_students = pickle.load(picklefile)

    Serializers.output_info(l_students, month)
