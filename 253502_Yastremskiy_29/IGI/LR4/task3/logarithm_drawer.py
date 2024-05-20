import matplotlib.pyplot as plt
import task3.logarithm_function
import numpy as np

class Drawer:
    step = 0.01
    def build_graphics(self, eps: float):
        """
        Building method for 2 plots: math.func() and Taylor series with specified accuracy.
        """
        test = task3.logarithm_function.LogarithmFunction()
        all_points = list()
        
        i : float = -0.99
        while i < 0.99:
            all_points.append(test.series_calculating(i, eps)[0])
            i += self.step
            
        params = test.get_parameters(all_points)
        x_range = np.linspace(-1, 1, len(all_points))
        y = self.log_func(x_range)
        
        plt.plot(x_range, y, label='y = ln(1-x)')
        plt.plot(x_range, all_points, label = 'Taylor series')
        plt.annotate(f'Avg_series_sum: {params[0]}\nMedian: {params[1]}\n\
Mode: {params[2]}\nDispersion: {params[3]}\nStandard deviation: {params[4]}',
            xy=(-0.75, -2), arrowprops=dict(facecolor='purple')) 
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.title('Graphics of function y = ln(1-x) with series calculating and math calculating')
        plt.savefig('logarithm_plot.png')
        plt.show()

    def log_func(self, x):
        """
        Function for correct building ln(1-x) using matplotlib.
        """
        return np.log(1 - x)


