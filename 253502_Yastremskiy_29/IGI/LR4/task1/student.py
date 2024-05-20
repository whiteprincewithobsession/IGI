from task1.human import Human
from task1.mixin_class import PrintableMixin

class Student(Human, PrintableMixin):
    def __init__(self, name : str, day : int, month : int, year : int, student_id : int):
        super().__init__(name, day, month, year)
        self.student_id = student_id
        
    @property
    def birth_date(self):
        """
        Property of birthday.
        """
        return self.year, self.month, self.day
    
    @birth_date.setter
    def birth_date(self, value : tuple[int, int, int]):
        """
        Setter of birthday.
        """
        if value.__sizeof__() < 3:
            raise ValueError("Wrong format of date!")
        self.day = value[2]
        self.month = value[1]
        self.year = value[0]
        
        
    
    
        
        