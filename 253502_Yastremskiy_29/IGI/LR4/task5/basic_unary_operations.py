class BasicUnaryOperations(object):
    def __init__(self, value):
        self.__value = value
        
    @property
    def value(self):
        """
        Property of value for unary operations.
        """
        return self.__value
    
    @value.setter
    def value(self, value):
        """
        Property of value for unary operations.
        """
        try:
            self.__value = value
        except:
            raise ValueError("Wrong format of value!")
    
