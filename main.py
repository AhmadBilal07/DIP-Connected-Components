#Importing Necessary Libraries
from PIL import Image,ImageDraw
import numpy as np
from collections import OrderedDict


#Path of the Image whose components are to be finded
IMG_PATH = "sample images/shapes4.png"

#Opening the img and converting it into Black and white
img = Image.open(IMG_PATH)
thresh = 220
fn = lambda x : 255 if x > thresh else 0
img = img.convert('L').point(fn, mode='1')



img.show()


#Converting img into array
data = np.asarray( img, dtype="int32" )
num_rows = np.shape(data)[0]
num_columns = np.shape(data)[1]

print("Image Dimensions:")
print("Rows : ",num_rows)
print("Columns : ",num_columns)


cc = 50
conflictedLabels = {}

#Finding Components
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
                    conflictedLabels[data[i-1][j]] = data[i][j - 1]
                elif data[i][j - 1] < data[i - 1][j]:
                    data[i][j] = data[i][j - 1]
                    conflictedLabels[data[i][j-1]] =  data[i-1][j ]
                else:
                    data[i][j] = data[i-1][j]

            if data[i-1][j] !=1 and data[i][j-1] == 1:
                data[i][j] = data[i-1][j]
            if data[i - 1][j] == 1 and data[i][j - 1] != 1:
                data[i][j] = data[i][j - 1]


#Sorting Dict in descending order
OrderedDict(sorted(conflictedLabels.items(), key=lambda t: t[0]))

#Re-Labelling
for key in reversed(list(conflictedLabels.keys())):
    data[data == conflictedLabels[key]] = key

#Getting Total  number of Components
totalComponents = np.unique(data)

#Excluding Background's count
componentsCount = totalComponents.__len__() - 1

print("Total Components: ", componentsCount)

'''
ComponentsCoordinate:
[componentNumber,ComponentColourValue,x1,y1,x2,y2]
'''

componentsList = []
#Finding Coordinates of Connected Components
for index,i in enumerate(totalComponents[1:]):
    arr = np.where(data == i)
    arr_Length_Xaxis = arr[0].__len__()
    arr_Length_Yaxis = arr[1].__len__()
    componentsList.append([index+1,i,arr[0][0],arr[1][0],arr[0][arr_Length_Xaxis-1],arr[1][arr_Length_Yaxis-1]])

print("Components List : ",componentsList)
img = Image.fromarray(data)
#img.show()


# Opening Original Image
img = Image.open(IMG_PATH)

#Drawing Bounding Box over the connected components:
for i in componentsList:
    draw = ImageDraw.Draw(img)
    draw.rectangle([i[3],i[2],i[5],i[4]],outline="#FFFF00")

img.show()
