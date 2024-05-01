import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

# Параметры сигнала
A0 = 1.0  # Амплитуда
w0 = 2.0  # Частота
phi0 = np.pi / 4  # Фаза

# Создание данных для построения графика
x = np.linspace(0, 10, 1000)
y = A0 * np.sin(w0 * x + phi0)

# Прямое преобразование Фурье
def fourier_transform(signal):
    N = len(signal)
    freqs = np.fft.fftfreq(N)
    fft_values = np.fft.fft(signal)
    return freqs, fft_values

freqs, fft_values = fourier_transform(y)

# Обратное преобразование Фурье
def inverse_fourier_transform(fft_values):
    signal = np.fft.ifft(fft_values)
    return signal

# Получение обратного преобразования Фурье
reconstructed_signal = inverse_fourier_transform(fft_values)

# Прямое преобразование Фурье с использованием библиотеки scipy.fft
fft_values_lib = fft(y)

# Обратное преобразование Фурье с использованием библиотеки scipy.fft
reconstructed_signal_lib = ifft(fft_values_lib)

# Построение всех графиков на одном
plt.figure(figsize=(12, 12))

# Исходный сигнал
plt.subplot(3, 1, 1)
plt.plot(x, y, label='Исходный сигнал', color='blue')
plt.legend()
plt.grid(True)
plt.text(7, 0.5, r'$f(x) = A_0 \sin(w_0 x + \phi_0)$', fontsize=14, color='black')

# Преобразование Фурье
plt.subplot(3, 1, 2)
plt.plot(freqs, np.abs(fft_values), label='Преобразование Фурье', color='green')
plt.legend()
plt.grid(True)
plt.text(0, 100, r'$F(\omega) = \mathcal{F}\{f(x)\}$', fontsize=14, color='black')

# Восстановленный сигнал с использованием прямого преобразования Фурье
plt.subplot(3, 1, 3)
plt.plot(x, np.real(reconstructed_signal), label='Восстановленный сигнал (без библиотеки)', color='red')
plt.legend()
plt.grid(True)
plt.text(7, 0.5, r'$\hat{f}(x) = \mathcal{F}^{-1}\{F(\omega)\}$', fontsize=14, color='black')

plt.tight_layout()
plt.show()

# Построение восстановленного сигнала с использованием библиотеки scipy.fft для сравнения
plt.figure(figsize=(10, 6))
plt.plot(x, np.real(reconstructed_signal_lib), label='Восстановленный сигнал (с библиотекой)', color='purple')
plt.title('Восстановленный сигнал (с библиотекой)')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid(True)
plt.text(7, 0.5, r'$\hat{f}(x) = \mathcal{F}^{-1}\{F(\omega)\}$', fontsize=14, color='black')
plt.show()
