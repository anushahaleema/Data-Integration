import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew
from tabulate import tabulate

print('Reading the final file')
df=pd.read_csv('final.csv', sep=',',header=None)
file1 = df.values
file1 = np.array(file1)

file1=np.delete(file1,[0,1],0)

for i in range(len(file1)):
    file1[i,1] = int(float(file1[i,1]))
    file1[i][2] = float(file1[i][2])

analysis = []
#calculating max
analysis.append(['max',np.max(file1[:,1]),np.max(file1[:,2])])
# calculating mean
analysis.append(['mean',np.mean(file1[:,1]),np.mean(file1[:,2])])
#calculating median
analysis.append(['median',np.median(file1[:,1]),np.median(file1[:,2])])
#calculating standard deviation
analysis.append(['standard deviation',np.std(file1[:,1]),np.std(file1[:,2])])
#calculating skewness
analysis.append(['skew',skew(file1[:,1]),skew(file1[:,2])])
#calculating kurtosis
analysis.append(['kurtosis',kurtosis(file1[:,1]),kurtosis(file1[:,2])])

print(tabulate(analysis, headers=['Parameter', 'Daily Cases', 'Cases Per million']))