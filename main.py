#Importing Necessary Libraries
from PIL import Image,ImageDraw
import numpy as np
from collections import OrderedDict,defaultdict


#Path of the Image whose components are to be found
IMG_PATH = "sample images/shapes.png"

#Opening the img and converting it into Black and white
img = Image.open(IMG_PATH)
thresh = 220
fn = lambda x : 255 if x > thresh else 0
img = img.convert('L').point(fn, mode='1')


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
                    conflictedLabels[data[i-1][j]] = (data[i][j - 1])
                elif data[i][j - 1] < data[i - 1][j]:
                    data[i][j] = data[i][j - 1]
                    conflictedLabels[data[i][j-1]] = (data[i-1][j ])
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
ComponentsList:
[componentNumber,x1,y1,x2,y2]
'''
componentsList = []



#Finding Coordinates of Connected Components
for index,i in enumerate(totalComponents[1:]):
    flag=0
    x1 = -1
    x2 = -1
    y1 = -1
    y2 = -1
    for j in range (num_rows):
        for k in range(num_columns):
            if data[j][k] == i:
                flag+=1
                if(flag == 1):
                    y1=j
                    x1 =k
                if(k < x1):
                    x1 = k
                if (k > x2):
                    x2 = k;
                y2 = j
    componentsList.append([index+1,x1,y1,x2,y2])


# Colouring Components
for index,i in enumerate(totalComponents[1:]):
    data[data == i] = (index+1)*25
img = Image.fromarray(data)
img.show()

print("Components List : ",componentsList)




# Opening Original Image
img = Image.open(IMG_PATH)

#Drawing Bounding Box over the connected components:
for i in componentsList:
    draw = ImageDraw.Draw(img)
    draw.rectangle([i[1],i[2],i[3],i[4]],outline="#FFFF00")

img.show()
