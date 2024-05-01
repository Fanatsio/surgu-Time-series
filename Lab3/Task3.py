import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path, delimiter="\t"):
    """
    Чтение данных из файла.

    Parameters:
    file_path (str): Путь к файлу.
    delimiter (str, optional): Разделитель данных в файле. По умолчанию '\t'.

    Returns:
    DataFrame: Прочитанные данные.
    """
    return pd.read_csv(file_path, delimiter=delimiter)

def convert_to_time_series(data):
    """
    Преобразование данных во временной ряд.

    Parameters:
    data (DataFrame): Входные данные.

    Returns:
    Series: Временной ряд (среднее значение по строкам).
    """
    return data.mean(axis=1)

def plot_time_series(time_series):
    """
    Визуализация временного ряда.

    Parameters:
    time_series (Series): Временной ряд.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(time_series, linestyle='-')
    plt.title('Изменение сердечного ритма во времени')
    plt.xlabel('Время')
    plt.ylabel('Интервал между ударами сердца (мс)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Чтение данных из файла
    data = read_data("lab3_data4.txt")

    # Преобразование данных во временной ряд
    time_series = convert_to_time_series(data)

    # Визуализация временного ряда
    plot_time_series(time_series)
