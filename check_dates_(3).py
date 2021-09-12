import pandas as pd
import numpy as np

print('Reading first file....')
df=pd.read_csv('data1.csv', sep=',',header=None)
file1 = df.values

print('Reading second file....')
df=pd.read_csv('data2.csv', sep=',',header=None)
file2 = df.values

# matching date
file1 = np.array(file1)
file2 = np.array(file2)

set1 = set()
set2 = set()
for i in file1:
    set1.add(i[0])
for i in file2:
    set2.add(i[0])

#check for any missing dates
set_final = set()
print('\nDates that are not in the second file but are present in the first file')
l1 = list(set1 - set2)
print(l1)
print('\nDates that are not in the first file but are present in the second file')
l2 = list(set2 - set1)
print(l2)
for i in l2:
    l1.append(i)
    print('')
for i in l1:
    set_final.add(i)

print('\nChecking both files and changing them as per requirement')
listf1delete = []
for i in range(len(file1)):
    if file1[i,0] in set_final or file1[i,0] == 0 or file1[i,0] == '0':
        listf1delete.append(i)

file1 = np.delete(file1,listf1delete,0)
#save file
print('\nSaving file....')
dataframe = pd.DataFrame(file1)
dataframe.to_csv("data1.csv",index=False)
print('File saved with the name data1.csv')

listf1delete = []
for i in range(len(file2)):
    if file2[i,0] in set_final or file2[i,0] == 0 or file2[i,0] == '0':
        listf1delete.append(i)

file2 = np.delete(file2,listf1delete,0)
#save file
print('\nSaving file....')
dataframe = pd.DataFrame(file2)
dataframe.to_csv("data2.csv",index=False)
print('File saved with the name data2.csv')