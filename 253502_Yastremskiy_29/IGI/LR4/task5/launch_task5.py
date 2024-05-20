from task5.matrix_unary_operations import MatrixUnaryOperations
from utils.checkers import input_size
from utils.random_generator import Generator

def start_task5() -> None:
    """
    Function for launching task #5.
    """
    print("To set size of matrix enter 1, else 2")
    ch = int(input())
    matrix = []
    if ch == 1:
        rows = input_size("rows", 0)
        columns = input_size("columns", 0)
        matrix = Generator.generate_random_matrix(rows, columns)
    else:
        matrix = Generator.generate_random_matrix()
    test_matrix = MatrixUnaryOperations(matrix)
    print(f"Original matrix:\n{matrix}")
    print(f"Sum below main diagonal: {test_matrix.sum_below_main_diagonal()}\n\
Manual standard deviation: {test_matrix.standard_deviation()}\nNumpy standard deviation: {test_matrix.numpy_standard_deviation()}")