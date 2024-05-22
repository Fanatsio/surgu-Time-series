import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из файла
filename = 'lab5_data4.txt'
time = []
signal1 = []
signal2 = []

with open(filename, 'r') as file:
    for line in file:
        parts = line.strip().split(';')
        time.append(int(parts[0]))
        signal1.append(float(parts[1]))
        signal2.append(float(parts[2]))

# Преобразование данных в numpy массивы
time = np.array(time)
signal1 = np.array(signal1)
signal2 = np.array(signal2)

# Выполнение преобразования Фурье
fft_signal1 = np.fft.fft(signal1)
fft_signal2 = np.fft.fft(signal2)

# Частотная шкала
n = len(time)
freq = np.fft.fftfreq(n, d=1)

print(freq)

# Амплитудные характеристики
amp_signal1 = np.abs(fft_signal1) / n
amp_signal2 = np.abs(fft_signal2) / n

# Фазовые характеристики
phase_signal1 = np.angle(fft_signal1)
phase_signal2 = np.angle(fft_signal2)

print(phase_signal1)
print(phase_signal2)

# Учет только положительных частот
positive_freq_indices = np.where(freq >= 0)

positive_freq = freq[positive_freq_indices]
amp_signal1 = amp_signal1[positive_freq_indices]
amp_signal2 = amp_signal2[positive_freq_indices]
phase_signal1 = phase_signal1[positive_freq_indices]
phase_signal2 = phase_signal2[positive_freq_indices]

# Построение графиков
plt.figure(figsize=(14, 10))

# АЧХ для первого сигнала
plt.subplot(2, 2, 1)
plt.plot(positive_freq, amp_signal1, 'b')
plt.title('АЧХ для сигнала 1')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')

# ФЧХ для первого сигнала
plt.subplot(2, 2, 2)
plt.plot(positive_freq, phase_signal1, 'b')
plt.title('ФЧХ для сигнала 1')
plt.xlabel('Частота (Гц)')
plt.ylabel('Фаза (рад)')

# АЧХ для второго сигнала
plt.subplot(2, 2, 3)
plt.plot(positive_freq, amp_signal2, 'r')
plt.title('АЧХ для сигнала 2')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')

# ФЧХ для второго сигнала
plt.subplot(2, 2, 4)
plt.plot(positive_freq, phase_signal2, 'r')
plt.title('ФЧХ для сигнала 2')
plt.xlabel('Частота (Гц)')
plt.ylabel('Фаза (рад)')

plt.tight_layout()
plt.show()
