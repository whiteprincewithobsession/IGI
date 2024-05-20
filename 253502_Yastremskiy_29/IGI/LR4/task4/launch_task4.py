from task4.regular_polygon import RegularPolygon
from utils.checkers import input_size, float_checker

def start_task4() -> None:
    """
    Function for launching task #4.
    """
    sides : int = input_size("number sides", 2)
    length : float = float_checker(1e-16, 1e16)
    color : str = input("Enter the color of figure: ")
    name : str = input("Enter the name of figure: ")
    text : str = input("Enter the text, that will be placed on the figure: ")
    test_figure = RegularPolygon(length, sides, color, name)
    test_figure.draw_regular_polygon(text)