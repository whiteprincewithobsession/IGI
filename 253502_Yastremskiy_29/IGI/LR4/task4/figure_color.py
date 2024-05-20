class FigureColor:
    def __init__(self, color : str):
        self._color = color
    
    @property
    def color(self) -> str:
        """
        Property of color.
        """
        return self._color
    
    @color.setter
    def color(self, value):
        """
        Setter of color.
        """
        self._color = value