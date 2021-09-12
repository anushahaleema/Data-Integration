import pandas as pd
from array import *
import main

print('Processing....')
df=pd.read_csv('covid2.csv', sep=',', header=None)
values = df.values

finalVal = [['cases','date','per_million']]
for i in values:
    if i[2] == 'India':
        finalVal.append([i[3],int(i[5]),float(i[11])])

# sorting 0 values
finalVal = main.calculateandSort0Value(finalVal)

# formatting time
finalValTimePrint = main.formatDate(finalVal, "%Y-%m-%d")

#formatting date and printing
main.plotTimeSeries(finalValTimePrint[1:, 0], finalValTimePrint[1:, 1], 1, 'Cases')
main.plotTimeSeries(finalValTimePrint[1:, 0], finalValTimePrint[1:, 2], 1, 'Cases Per million')

#save file
print('\nSaving file...')
dataframe = pd.DataFrame(finalVal)
dataframe.to_csv("data2.csv",index=False)
print('File saved with the name data2.csv')