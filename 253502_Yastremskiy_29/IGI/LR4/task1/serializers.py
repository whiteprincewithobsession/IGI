import csv
import pickle
from task1.student import Student

class Serializers:
    @staticmethod
    def serialize_to_csv(students, filename):
        """
        Static method for converting list of students to *.csv file
        """
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'day', 'month', 'year', 'student_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students.values():
                writer.writerow({'name': student.name,
                             'day': student.day,
                             'month': student.month,
                             'year': student.year,
                             'student_id': student.student_id})
            
    @staticmethod
    def serialize_to_pickle(students, filename):
        """
        Serialize list of students to *.pkl file.
        """
        with open(filename, 'wb') as picklefile:
            pickle.dump(students, picklefile)

    @staticmethod
    def load_from_csv(filename):
        """
        Load students from *.csv file.
        """
        students = []
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(Student(row['name'], int(row['day']), int(row['month']), int(row['year']), int(row['student_id'])))
        return students
    
    @staticmethod
    def output_info(loaded_students : any, month : int) -> None: 
        
        filtered_students = [student for student in loaded_students.values() if student.month == month]
        
        print(f"Students, who was born in the month={month}:")
        if(len(filtered_students) == 0):
            print("No students with such month\n")
        else:
            for student in filtered_students:
                print(f"{student.name}, ID: {student.student_id}, Birth date: {student.day:02}.{student.month:02}.{student.year:4}")

        print("\nInfo from *.csv file with sorting by field=name:\n")
        loaded_students = Serializers.load_from_csv('students.csv')
        
        filtered_students = [student for student in loaded_students if student.month == month]

        sorted_students = sorted(filtered_students, key=lambda x: x.name)
        print(f"Students, who was born in the month={month}, sorted by name:")
        if(len(filtered_students) == 0):
            print("No students with such month\n")
        else:
            for student in sorted_students:
                print(f"{student.name}, ID: {student.student_id}, Birth date: {student.day:02}.{student.month:02}.{student.year}")