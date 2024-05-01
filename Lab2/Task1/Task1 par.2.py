import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

def step_signal(x):
    """
    Генерация ступенчатого сигнала.

    Parameters:
    x (ndarray): Массив значений x.

    Returns:
    ndarray: Ступенчатый сигнал.
    """
    return np.where((0 <= x) & (x < 1), 1, 0)

def convolution_plot(x, f, g):
    """
    Построение графика свертки двух сигналов.

    Parameters:
    x (ndarray): Массив значений x.
    f (ndarray): Первый сигнал.
    g (ndarray): Второй сигнал.

    Returns:
    None
    """
    conv_result = convolve(f, g, mode='full')
    
    plt.figure(figsize=(10, 5))

    plt.subplot(3, 1, 1)
    plt.plot(x, f, 'b', label='f(x)')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(x, g, 'g', label='g(x)')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(conv_result, 'r', label='f(x) * g(x)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Задание диапазона x
    x = np.arange(-2, 5, 0.01)

    # Генерация ступенчатых сигналов
    f_signal = step_signal(x)
    g_signal = step_signal(x)

    # Построение графика свертки сигналов
    convolution_plot(x, f_signal, g_signal)
