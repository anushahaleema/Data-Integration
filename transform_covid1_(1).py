
import pandas as pd
import main

print('Processing....')
df=pd.read_csv('covid1.csv', sep=',', header=None)
values = df.values

# removing first column --> since it contains null values
values = values[:,1:]

#  filtering country as India
val=[]
for i in values:
    if i[0] == 'India':
        val = i
        break

# converting column data to row data
finalVal = [['cases','date']]
for column in range(len(values[0])):
    finalVal.append([values[0][column],val[column]])

#removing country , latitude & longitude
del(finalVal[1])
del(finalVal[1])
del(finalVal[1])

#getting cases per day
finalVal = main.calculateCasesPerDay(finalVal)

#processing 0
finalVal = main.calculateandSort0Value(finalVal)

print("\nformatting time and plotting")

#formatting date
finalValTimePrint = main.formatDate(finalVal, "%m/%d/%y")

#formatting date and printing
main.plotTimeSeries(finalValTimePrint[1:, 0], finalValTimePrint[1:, 1], 1, 'cases')

#save file
print('\nSaving file...')
dataframe = pd.DataFrame(finalVal)
dataframe.to_csv("data1.csv",index=False)
print('File saved with the name data1.csv')