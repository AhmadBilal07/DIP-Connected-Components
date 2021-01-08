from PIL import Image
import numpy as np
from collections import OrderedDict

IMG_PATH = "sample images/shapes2.png"

#Opening the img and converting it to Black and white
img = Image.open(IMG_PATH).convert(mode="1", dither=Image.NONE)


#Converting img into array

data = np.asarray( img, dtype="int32" )
num_rows = np.shape(data)[0]
num_columns = np.shape(data)[1]


print("Rows : ",num_rows)
print("Columns : ",num_columns)


cc = 50
conflictedlabels = {}

for i in range(num_rows):
    for j in range (num_columns):

        if data[i][j] == 1:
            data[i][j] = 1

        if data[i][j] == 0:
            if data [i-1][j] == 1 and data[i][j-1] == 1:
                cc = cc + 20;
                data[i][j] = cc;

            if data[i - 1][j] != 1 and data[i][j - 1] != 1:
                if data[i - 1][j] < data[i][j - 1]:
                    data[i][j] = data[i - 1][j]
                    conflictedlabels[data[i-1][j]] = data[i][j - 1]
                elif data[i][j - 1] < data[i - 1][j]:
                    data[i][j] = data[i][j - 1]
                    conflictedlabels[data[ i][j-1]] =  data[i-1][j ]
                else:
                    data[i][j] = data[i-1][j]

            if data[i-1][j] !=1 and data[i][j-1] == 1:
                data[i][j] = data[i-1][j]
            if data[i - 1][j] == 1 and data[i][j - 1] != 1:
                data[i][j] = data[i][j - 1]


#Sorting Dict in descending order
OrderedDict(sorted(conflictedlabels.items(), key=lambda t: t[0]))

#Re-Labelling
for key in reversed(list(conflictedlabels.keys())):
    data[data == conflictedlabels[key]] = key

componentsCount = np.unique(data)
print("Total Components: ", componentsCount.__len__() - 1)

img = Image.fromarray(data)

img.show()


