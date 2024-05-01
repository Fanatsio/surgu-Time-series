import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    """Загрузка данных из файла"""
    data = np.genfromtxt(file_path, delimiter=';', skip_header=1)
    return data[:, 0], data[:, 1], data[:, 2]

def plot_amplitude_frequency(frequency, amplitude):
    """Построение графика АЧХ"""
    plt.plot(frequency, amplitude)
    plt.title('Амплитудно-частотная характеристика')
    plt.xlabel('Частота')
    plt.ylabel('Амплитуда')
    plt.grid()

def plot_phase_frequency(frequency, phase):
    """Построение графика ФЧХ"""
    plt.plot(frequency, phase)
    plt.title('Фазо-частотная характеристика')
    plt.xlabel('Частота')
    plt.ylabel('Фаза')
    plt.grid()

def main():
    frequency, amplitude, phase = load_data('lab5_data4.txt')
    
    plt.figure(figsize=(10, 6))
    
    plt.subplot(2, 1, 1)
    plot_amplitude_frequency(frequency, amplitude)

    plt.subplot(2, 1, 2)
    plot_phase_frequency(frequency, phase)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
