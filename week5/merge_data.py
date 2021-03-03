import glob
import numpy as np
import pandas as pd

file_list = []
for filename in glob.iglob("./F/" + "**/*.txt", recursive=True):
    file_list.append(filename)
for filename in glob.iglob("./N/" + "**/*.txt", recursive=True):
    file_list.append(filename)
for filename in glob.iglob("./O/" + "**/*.txt", recursive=True):
    file_list.append(filename)
for filename in glob.iglob("./S/" + "**/*.txt", recursive=True):
    file_list.append(filename)
for filename in glob.iglob("./Z/" + "**/*.txt", recursive=True):
    file_list.append(filename)


file_list.sort()
# print(file_list)


# file_content_data = [[]]
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
