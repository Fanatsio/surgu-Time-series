import numpy as np
import matplotlib.pyplot as plt

# Определение новых математических функций
def logarithm(x):
    return np.log(x + 1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def cubic(x):
    return x ** 3

def tangent(x):
    return np.tan(x)

def square_root(x):
    return np.sqrt(np.abs(x))

# Создание массива значений x
x = np.linspace(-5, 5, 100)

# Построение графиков функций
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot(x, logarithm(x), label='ln(x + 1)')
plt.plot(x, sigmoid(x), label='1 / (1 + e^(-x))')
plt.legend()
plt.title('Logarithm vs Sigmoid')

plt.subplot(3, 2, 2)
plt.plot(x, np.correlate(logarithm(x), sigmoid(x), mode='same'), label='Cross-Correlation')
plt.legend()
plt.title('Cross-Correlation: ln(x + 1) and sigmoid(x)')

plt.subplot(3, 2, 3)
plt.plot(x, cubic(x), label='x^3')
plt.plot(x, tangent(x), label='tan(x)')
plt.legend()
plt.title('Cubic vs Tangent')

plt.subplot(3, 2, 4)
plt.plot(x, np.correlate(cubic(x), tangent(x), mode='same'), label='Cross-Correlation')
plt.legend()
plt.title('Cross-Correlation: x^3 and tan(x)')

plt.subplot(3, 2, 5)
plt.plot(x, square_root(x), label='sqrt(|x|)')
plt.plot(x, cubic(x), label='x^3')
plt.legend()
plt.title('Square Root vs Cubic')

plt.subplot(3, 2, 6)
plt.plot(x, np.correlate(square_root(x), cubic(x), mode='same'), label='Cross-Correlation')
plt.legend()
plt.title('Cross-Correlation: sqrt(|x|) and x^3')

plt.tight_layout()
plt.show()
