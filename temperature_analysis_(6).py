from numpy.lib import utils
import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew
from tabulate import tabulate
import main


print('Reading final file')
df=pd.read_csv('data_temp_italy.csv', sep=',',header=None)
file1 = df.values
file1 = np.array(file1)

file1 = main.formatDate(file1, "%Y-%m-%d")
file1 = main.formatTemp(file1)

#plotting cases vs temp
main.plotTimeSeries2(file1[:, 0], file1[:, 1], file1[:, 2], 1, 'temp', 'cases')
for i in range(len(file1)):
    file1[i][1] = int(file1[i][1])

