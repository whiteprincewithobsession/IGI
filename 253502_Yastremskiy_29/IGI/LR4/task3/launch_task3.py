from utils.checkers import float_checker
from task3.logarithm_function import LogarithmFunction
from task3.logarithm_drawer import Drawer 
def start_task3()-> None:
    """
    Function for launching task #3.
    """
    print("Enter accuracy of Taylor series...")
    eps = float_checker(0, 1)
    func = LogarithmFunction()
    plot = Drawer()
    plot.build_graphics(eps)