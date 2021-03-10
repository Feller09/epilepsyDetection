#import glob
import numpy as np
import pandas as pd
from pathlib import Path

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []


print("Added files from F to list ")
for filename in Path("./F").rglob("*.txt"):
    list1.append(filename)

print(len(list1))
print("Added files from N to list ")
for filename in Path("./N").rglob("*.TXT"):
    list2.append(filename)

print(len(list2))


print("Added files from O to list ")
for filename in Path("./O").rglob("*.txt"):
    list3.append(filename)


print("Added files from S to list ")
for filename in Path("./S").rglob("*.txt"):
    list4.append(filename)


print("Added files from Z to list ")
for filename in Path("./Z").rglob("*.txt"):
    list5.append(filename)    

file_list=[]

print("Adding files 1")
for i in list1:
	file_list.append(i)

print("Adding files 2")
for i in list2:
	file_list.append(i)

print("Adding files 3")
for i in list3:
	file_list.append(i)

print("Adding files 4")
for i in list4:
	file_list.append(i)

print("Adding files 5")
for i in list5:
	file_list.append(i)


# file_content_data = [[]]
print(len(file_list))
file_content = []
numpy_list = []

try:
    for i in file_list:
        lines = ""
        arr = ""
        with open(i) as f:
            lines = f.readlines()
            file_content = [x.strip() for x in lines]
            arr = np.asarray(file_content)
        numpy_list.append(arr)
    numpy_list = np.asmatrix(numpy_list)
    print(numpy_list)
    print(numpy_list.shape)
    # now writing to a file
    DF = pd.DataFrame(numpy_list)
    DF.to_csv("data3.csv")
    print("Written to file")

except Exception as e:
    print(e)
