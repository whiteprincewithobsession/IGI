from task4.geometric_figure import GeometricFigure
from task4.figure_color import FigureColor
from math import sin, cos, pi
import matplotlib.pyplot as plt

class RegularPolygon(GeometricFigure):
    def __init__(self, side_length : float, number_sides : int, color : str, name: str):
        """
        __init__
        Args:
            side_length (float): length of side.
            number_sides (int): number of sides in polygon.
            color (str): color of plot.
            name (str): name that will be displayed on the plot.
        """
        self._side_length = side_length
        self._number_sides = number_sides
        self._color = FigureColor(color)
        self._name = name
    
    def get_parameters(self):
        """
        Function for getting parameters of n-gon(num of sides, color, area, name).
        """
        return "Side length: {}\nNumber of sides: {}\nColor of figure: {}\nArea: {}\nName: {}".format(self._number_sides,
            self._side_length, self._color.color, self.area(), self.name)
    
    def area(self) -> float:
        """
        Function for calculating area of regular n-gon.
        """
        first_part : float = self._side_length* self._side_length * self._number_sides / 4
        cotan : float = cos(pi / self._number_sides) / sin(pi / self._number_sides)
        return first_part * cotan

    def draw_regular_polygon(self, text : str):
        """
        Function for drawing n-gon with current text.
        """
        x_center, y_center = 0, 0
        r = self._side_length / (2 * sin(pi / self._number_sides))
        coords = [(x_center + r * cos(2 * pi * i / self._number_sides), y_center + r * sin(2 * pi * i / self._number_sides)) for i in range(self._number_sides)]

        coords.append(coords[0])
        plt.figure(figsize=(6, 6))
        plt.axis('equal')
        plt.grid()
        plt.title(f"Regular {self._number_sides}-polygon with side length: {self._side_length}\nName: {self.name}")
        try:
            plt.plot(*zip(*coords), marker='o', markersize=8, linestyle='-', color=self._color.color)
            plt.fill(*zip(*coords), alpha=0.6, color= self._color.color)
            plt.savefig('regular_polygon.png')
            plt.text(0, 0, text, fontsize=9, color='black')
            plt.show()
        except ValueError as e:
            print(f"Something went wrong: {e}")
            
    @property
    def color(self) -> str:
        """
        Property of color.
        """
        return self._color.color
    
    @color.setter
    def color(self, value : str):
        """
        Setter of color.
        """
        self._color.color = value
        
    @property
    def name(self) -> str:
        """
        Property of name.
        """
        return self._name
    
    @name.setter
    def name(self, value : str):
        """
        Setter of color.
        """
        self._name = value
