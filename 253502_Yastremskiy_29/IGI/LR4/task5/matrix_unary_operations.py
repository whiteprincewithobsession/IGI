import numpy as np
from task5.basic_unary_operations import BasicUnaryOperations
from math import sqrt

class MatrixUnaryOperations(BasicUnaryOperations):
    def __init__(self, value):
        super().__init__(value)
        
    def sum_below_main_diagonal(self)->float:
        """
        Calculates sum of elements below main diagonal in matrix
        """
        return np.sum(np.tril(self.value, k=-1))
    
    def numpy_standard_deviation(self) -> float:
        """
        Finds standard deviation of elements situated on the main diagonal of matrix.
        Uses numpy.
        """
        return round(np.std(np.diag(self.value)), 2)
    
    def standard_deviation(self) -> float:
        """
        Finds standard deviation of elements situated on the main diagonal of matrix.
        Works manually.
        """
        diag_elem = np.diag(self.value)
        avg_sum_of_squares = sum(x**2 for x in diag_elem) / diag_elem.size
        avg_square_sum = (sum(diag_elem) / diag_elem.size)**2
        return round(sqrt(avg_sum_of_squares - avg_square_sum), 2)
