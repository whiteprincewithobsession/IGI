class PrintableMixin:
    def print_info(self) -> None:
        """
        Get full info about student.
        """
        print(f"Name: {self._name}, Date of birth: {str(self._day).zfill(2)}.{str(self._month).zfill(2)}.{str(self._year).zfill(4)}")
