import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    Определение ступенчатого сигнала f(x).

    Parameters:
    x (ndarray): Входной массив значений.

    Returns:
    ndarray: Результат функции f(x).
    """
    return np.where((0 <= x) & (x < 1), 1, 0)

def g(x):
    """
    Определение ступенчатого сигнала g(x).

    Parameters:
    x (ndarray): Входной массив значений.

    Returns:
    ndarray: Результат функции g(x).
    """
    return np.where((0 <= x) & (x < 1), 1, 0)

def convolution(f, g):
    """
    Реализация свёртки двух функций.

    Parameters:
    f (ndarray): Первая функция.
    g (ndarray): Вторая функция.

    Returns:
    ndarray: Результат свёртки f и g.
    """
    N = len(f)
    M = len(g)
    result = np.zeros(N + M - 1)
    
    for n in range(N):
        for m in range(M):
            result[n + m] += f[n] * g[m]
            
    return result

if __name__ == "__main__":
    # Задание диапазона x
    x = np.arange(-2, 5, 0.01)

    # Вычисление значений функций f(x) и g(x)
    f_values = f(x)
    g_values = g(x)

    # Вычисление свёртки
    conv_result = convolution(f_values, g_values)

    # Построение графиков
    plt.figure(figsize=(10, 5))

    plt.subplot(3, 1, 1)
    plt.plot(x, f_values, 'b', label='f(x)')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(x, g_values, 'g', label='g(x)')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(conv_result, 'r', label='f(x) * g(x)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
