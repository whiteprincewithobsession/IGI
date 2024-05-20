import numpy as np

class Generator:
    basic_size = 5, 5
    
    @staticmethod
    def generate_random_matrix(rows=basic_size[0], cols=basic_size[1]) -> list:
        return np.random.randint(low=0, high=100, size=(rows, cols))
