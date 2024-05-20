from math import log, sqrt
from collections import Counter
from task3.basic_function import Function
import statistics

class LogarithmFunction(Function):
    
    def math_calculating(self, x : float) -> float:
        """
        Calculates ln(1-x) using math
        """
        return log(1-x)
    
    def series_calculating(self, x: float, eps: float):
        """
        Calculates ln(1-x) in the specified X with accuracy using Taylor series.
        """
        logarithm_function = log(1 - x)
        series_values : list[float] = []
        current_sum = 0
        n = 0
        while n + 1 < 500:
            n += 1
            current_sum += (-1) * x**n / n
            series_values.append(current_sum)
            if abs(current_sum - logarithm_function) >= eps:
                continue
            break
        return current_sum, logarithm_function, n + 1, series_values
    
    def avg_sum_of_terms(self, terms : list[float]) -> float:
        """
        Calculates average sum of points(y).
        """
        return statistics.mean(terms)
    
    def median(self, terms : list[float]) -> float:
        """
        Find median of points(y).
        """
        # n = len(terms)
        # avg_index = n // 2
        # if n % 2 == 0:
        #     return sorted(terms)[avg_index]
        # return sum(sorted(terms)[avg_index - 1 : avg_index + 1]) / 2
        return statistics.median(terms)
    
    def mode(self, terms : list[float]) -> float:
        """
        Find mode of points(y).
        """
        # value_counts = Counter(terms)
        # max_count = max(value_counts.values())
        # all_modes = [value for value, count in value_counts.items() if count == max_count]
        return statistics.mode(terms)
    
    def dispersion(self, terms : list[float]) -> float:
        """
        Find dispersion of points(y).
        """
        # avg_sum = sum(terms) / len(terms)
        # square_difference = sum((x - avg_sum) ** 2 for x in terms)
        # disp = square_difference / len(terms)
        # return disp 
        return statistics.variance(terms)
    
    def standard_deviation(self, terms : list[float]) -> float:
        """
        Find standard deviation of points(y).
        """
        # return sqrt(self.dispersion(terms))
        return statistics.stdev(terms)
    
    def get_parameters(self, terms):
        """
        Return tuple of parameters above.
        """
        return self.avg_sum_of_terms(terms), self.median(terms),\
            self.mode(terms), self.dispersion(terms), self.standard_deviation(terms)
        