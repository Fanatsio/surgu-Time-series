import os
from data import Data
from analysis import Analysis


file_path = 'EuStockMarkets.csv'
data = Data(file_path)

while True:
    item = Analysis.menu()

    if item == 0:
        break
    elif item == 1:
        Analysis.plot_graph(data.DAX_values, data.SMI_values, data.CAC_values, data.FTSE_values)
    elif item == 2:
        Analysis.correlation_matrix(data.file, ['CAC', 'DAX', 'FTSE', 'SMI'])
    elif item == 3:
        Analysis.histograms_of_average_values(data.file, ['CAC', 'DAX', 'FTSE', 'SMI'])
    elif item == 4:
        Analysis.histogram_of_variance(data.file, ['CAC', 'DAX', 'FTSE', 'SMI'])
    elif item == 5:
        Analysis.histograms_of_absolute_values(data.DAX_values, data.SMI_values, data.CAC_values, data.FTSE_values)
    elif item == 6:
        Analysis.histograms_of_difference_values(data.DAX_values, data.SMI_values, data.CAC_values, data.FTSE_values)
    elif item == 7:
        Analysis.scatterplot_without_shift(data.DAX_values, data.SMI_values)
    elif item == 8:
        Analysis.scatterplot_with_shift(data.DAX_values, data.SMI_values)
    elif item == 9:
        Analysis.covariance_matrix(data.DAX_values, data.SMI_values)
    
    os.system('CLS')
