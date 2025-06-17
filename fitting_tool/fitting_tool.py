import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# === Define fitting functions ===
def linear(x, a, b):
    return a * x + b

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

def gaussian(x, a, x0, sigma):
    return a * np.exp(-((x - x0) ** 2) / (2 * sigma ** 2))

def sqrt_exponential(x,A,B,T1):
    return A+B*np.exp(-x/(2*T1))

def exponential(x,A,B,T1):
    return A+B*np.exp(-x/(2*T1))



# === Dictionary of available functions ===
FIT_FUNCTIONS = {
    'linear': linear,
    'quadratic': quadratic,
    'gaussian': gaussian,
}

# === Fit Controller Object ===
class FitTool:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.function_name = None
        self.popt = None
        self.pcov = None

    def choose_function(self, name):
        if name not in FIT_FUNCTIONS:
            raise ValueError(f"Function '{name}' not available. Choose from {list(FIT_FUNCTIONS.keys())}")
        self.function_name = name

    def fit(self, p0=None):
        if not self.function_name:
            raise RuntimeError("No fitting function chosen. Use 'choose_function' first.")
        func = FIT_FUNCTIONS[self.function_name]
        self.popt, self.pcov = curve_fit(func, self.x, self.y, p0=p0)
        return self.popt

    def plot(self):
        if self.popt is None:
            raise RuntimeError("Fit not performed yet. Call 'fit' first.")
        func = FIT_FUNCTIONS[self.function_name]
        plt.scatter(self.x, self.y, label='Data')
        x_fit = np.linspace(min(self.x), max(self.x), 500)
        y_fit = func(x_fit, *self.popt)
        plt.plot(x_fit, y_fit, label=f'Fit: {self.function_name}')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Fit Result')
        plt.show()
    def function_list(FIT_FUNCTIONS):
        return  print(str(FIT_FUNCTIONS))
