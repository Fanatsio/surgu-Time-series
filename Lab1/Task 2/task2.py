import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv("AirQualityUCI.csv", sep=";")

# Вывод первых нескольких строк данных
print(data.head())

# Преобразование данных в числовой формат (замена запятых на точки и приведение к float)
data['CO(GT)'] = data['CO(GT)'].str.replace(',', '.').astype(float)

# Визуализация временного ряда
plt.plot(data['CO(GT)'])
plt.xlabel('Time')
plt.ylabel('CO(GT)')
plt.title('CO(GT) Time Series')
plt.show()
