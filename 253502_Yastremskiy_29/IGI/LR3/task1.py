from math import log

def series_calculating(x: float, eps: float) -> tuple[float, float, int]:
    """
    Function  to compute the value of a math function by factoring into a power series
    ln(1-x) with a precision
    """
    logarithm_function = log(1 - x)
    current_sum = 0
    n = 0
    while n + 1 < 500:
        n += 1
        current_sum += (-1) * x**n / n
        if abs(current_sum - logarithm_function) >= eps:
            continue
        break
    return current_sum, logarithm_function, n + 1