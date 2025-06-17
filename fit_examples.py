from fitting_tool.fitting_tool import FitTool
import numpy as np

# Simulate some noisy Gaussian data
x = np.linspace(-5, 5, 50)
y = 3 * np.exp(-((x - 1)**2) / (2 * 1.5**2)) + 0.2 * np.random.normal(size=len(x))

# Initialize and use the tool
ft = FitTool(x, y)
ft.choose_function('gaussian')
params = ft.fit(p0=[1, 0, 1])  # optional: initial guess
print("Fitted Parameters:", params)
ft.plot()
