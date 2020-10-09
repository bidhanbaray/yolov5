import pandas as pd
import numpy as np
import os
import shutil

classes = ['ambulance','army vehicle','auto rickshaw','bicycle','bus','car','garbagevan','human hauler','minibus','minivan','motorbike','pickup','policecar','rickshaw','scooter','suv','taxi','three wheelers (CNG)','truck','van','wheelbarrow']


os.mkdir('output/images')
os.mkdir('output/labels')

fileNames = os.listdir('output/')
for file in fileNames:
    if file[-3:]=='jpg':
        shutil.move("output/"+file, "output/images/"+file)
    elif file[-3:]=='txt':
        shutil.move("output/"+file, "output/labels/"+file)
    else:
        continue

textLabels = os.listdir('output/labels')

df = pd.DataFrame(columns = ['image_id', 'class','score','xmin','ymin','xmax','ymax'])
for oneImage in textLabels:
    subdf = pd.read_csv("output/labels/"+oneImage, header = None,delim_whitespace=True)
    subdf['imageID'] = oneImage[:-4]
    for i, eachObject in subdf.iterrows():
        conf = round(float(eachObject[5]),2)
        new_row = {'image_id': eachObject['imageID'], 'class':classes[eachObject[0]],'score':conf,'xmin':eachObject[1],'ymin':eachObject[2],'xmax': eachObject[3],'ymax':eachObject[4]}
        df= df.append(new_row, ignore_index=True)
df['width'] = 1024
df['height'] = 1024
df.to_csv('result.csv',index = False)
