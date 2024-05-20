import abc

class GeometricFigure(abc.ABC):
    @abc.abstractmethod
    def area(self) -> float:
        """
        Abstract method for calculating area.
        """
        pass