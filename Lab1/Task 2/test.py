import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.graphics.tsaplots import plot_pacf

# Загрузка данных
data = pd.read_csv("AirQualityUCI.csv", sep=";")
data['CO(GT)'] = data['CO(GT)'].str.replace(',', '.').astype(float)

# Проверка наличия пропущенных значений в данных
print("Пропущенные значения в данных:")
print(data.isnull().sum())

# Обработка пропущенных значений (например, удаление строк с пропущенными значениями)
data.dropna(inplace=True)

# Определение лага с помощью графика частичной автокорреляционной функции (PACF)
plot_pacf(data['CO(GT)'], lags=50)
plt.xlabel('Lag')
plt.ylabel('Partial Autocorrelation')
plt.title('Partial Autocorrelation Function (PACF) for CO(GT) Time Series')
plt.show()

# Создание и обучение модели AR
lag = 5  # Выбор лага на основе анализа PACF
model = AutoReg(data['CO(GT)'], lags=lag)
model_fit = model.fit()

# Прогнозирование следующих значений ряда
forecast = model_fit.predict(start=len(data), end=len(data)+10, dynamic=False)

# Вывод прогнозируемых значений
print("Прогнозы:")
print(forecast)

# Построение графика прогноза
plt.plot(data['CO(GT)'], label='Actual')
plt.plot(np.arange(len(data), len(data)+11), forecast, label='Forecast')
plt.xlabel('Time')
plt.ylabel('CO(GT)')
plt.title('AR Model Forecasting CO(GT)')
plt.legend()
plt.show()
