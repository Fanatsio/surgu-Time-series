import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Analysis:
    @staticmethod
    def menu():
        print("Лабораторная работа №1 \n"
              "1 - Построить графики всех переменных\n"
              "2 - Построить матрицу корреляции \n"
              "3 - Построить гистограмму средних значений \n"
              "4 - Построить гистограмму дисперсии \n"
              "5 - Построить гистограмму абсолютных значений \n"
              "6 - Построить гистограмму разностей \n"
              "7 - Построить диаграмму рассеяния без смещения по времени \n"
              "8 - Построить диаграмму рассеяния со смещением по времени \n"
              "9 - Построить ковариационную матрицу \n"
              "0 - Выход")
        menu_item = int(input("Enter >> "))
        return menu_item

    @staticmethod
    def plot_graph(DAX_values, SMI_values, CAC_values, FTSE_values):
        plt.plot(DAX_values, color='blue', label='DAX')
        plt.plot(SMI_values, color='red', label='SMI')
        plt.plot(CAC_values, color='green', label='CAC')
        plt.plot(FTSE_values, color='orange', label='FTSE')
        plt.legend()
        plt.title('Graph')
        plt.xlabel('Number of Days')
        plt.ylabel('Data')
        plt.grid(True)
        plt.show()

    @staticmethod
    def correlation_matrix(df, columns):
        matrix = df[columns].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Matrix')
        plt.show()

    @staticmethod
    def histograms_of_average_values(df, columns):
        means = df[columns].mean()
        plt.figure(figsize=(10, 5))
        plt.bar(means.index, means.values, color='blue')
        plt.xlabel('Columns')
        plt.ylabel('Mean Value')
        plt.title('Average Values of Columns')
        plt.xticks(rotation=45)
        plt.show()

    @staticmethod
    def histogram_of_variance(df, columns):
        variances = df[columns].var()
        plt.figure(figsize=(10, 5))
        plt.bar(variances.index, variances.values, color='red')
        plt.xlabel('Columns')
        plt.ylabel('Variance')
        plt.title('Variances of Columns')
        plt.xticks(rotation=45)
        plt.show()

    @staticmethod
    def histograms_of_absolute_values(DAX_values, SMI_values, CAC_values, FTSE_values):
        plt.figure(figsize=(10, 6))
        plt.hist(DAX_values.abs(), bins=60, color='skyblue', edgecolor='black', alpha=0.7, label='DAX')
        plt.hist(SMI_values.abs(), bins=60, color='salmon', edgecolor='black', alpha=0.7, label='SMI')
        plt.hist(CAC_values.abs(), bins=60, color='green', edgecolor='black', alpha=0.7, label='CAC')
        plt.hist(FTSE_values.abs(), bins=60, color='purple', edgecolor='black', alpha=0.7, label='FTSE')
        plt.title('Histogram of Absolute Values')
        plt.xlabel('Absolute Value')
        plt.ylabel('Count')
        plt.legend()
        plt.grid(True)
        plt.show()

    @staticmethod
    def histograms_of_difference_values(DAX_values, SMI_values, CAC_values, FTSE_values):
        plt.figure(figsize=(10, 6))
        plt.hist(DAX_values.diff().dropna(), bins=60, color='skyblue', edgecolor='black', alpha=0.7, label='DAX')
        plt.hist(SMI_values.diff().dropna(), bins=60, color='salmon', edgecolor='black', alpha=0.7, label='SMI')
        plt.hist(CAC_values.diff().dropna(), bins=60, color='green', edgecolor='black', alpha=0.7, label='CAC')
        plt.hist(FTSE_values.diff().dropna(), bins=60, color='purple', edgecolor='black', alpha=0.7, label='FTSE')
        plt.title('Histogram of Differences')
        plt.xlabel('Difference')
        plt.ylabel('Count')
        plt.legend()
        plt.grid(True)
        plt.show()

    @staticmethod
    def scatterplot_without_shift(DAX_values, SMI_values):
        plt.figure(figsize=(8, 6))
        plt.scatter(DAX_values, SMI_values, color='skyblue', alpha=0.7)
        plt.title('Scatterplot of DAX and SMI')
        plt.xlabel('DAX')
        plt.ylabel('SMI')
        plt.grid(True)
        plt.show()

    @staticmethod
    def scatterplot_with_shift(DAX_values, SMI_values):
        lag_smi = SMI_values.shift(1)
        diff_smi = lag_smi.diff()
        diff_dax = DAX_values.diff()
        plt.figure(figsize=(8, 6))
        plt.scatter(diff_smi, diff_dax, color='skyblue', alpha=1)
        plt.title('Scatterplot with Shift')
        plt.xlabel('Difference in SMI with Shift')
        plt.ylabel('Difference in DAX')
        plt.grid(True)
        plt.show()

    @staticmethod
    def covariance_matrix(DAX_values, SMI_values):
        cov_matrix = np.cov(DAX_values, SMI_values)
        std_x = np.std(DAX_values)
        std_y = np.std(SMI_values)
        corr_matrix = cov_matrix / (std_x * std_y)
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
        plt.title('Covariance Matrix')
        plt.xlabel('DAX')
        plt.ylabel('SMI')
        plt.show()
