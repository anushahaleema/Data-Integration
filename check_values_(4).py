import pandas as pd
import numpy as np

print('Reading first file')
df=pd.read_csv('data1.csv', sep=',',header=None)
file1 = df.values

print('Reading second file')
df=pd.read_csv('data2.csv', sep=',',header=None)
file2 = df.values

# matching date
file1 = np.array(file1)
file2 = np.array(file2)
file1 = np.delete(file1,[0,1],0)
file2 = np.delete(file2,[0,1],0)

#checking values
map1 = dict()
for i in file1:
    map1[i[0]] = i[1]

map2 = dict()
for i in file2:
    map2[i[0]] = [i[1],i[2]]

print('\nCalculating the mismatching values')
c = 0
for i in map1:
    val = map2[i]
    if map1[i] != val[0]:
        c = c+1
finalVal = [['date','cases','per_million']]

#if no mismatch then add values to a final file
print('\nFinal file for printing')
if c == 0:
    for i in map1:
        finalVal.append([i,map1[i],map2[i][1]])

#save file
print('\nSaving file....')
dataframe = pd.DataFrame(finalVal)
dataframe.to_csv("final.csv",index=False)
print('File saved with the name final.csv')