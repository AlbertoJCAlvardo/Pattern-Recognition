# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:15:27 2022

@author: argen
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io,color


img = io.imread('francia.png',as_gray=True)

listed_image = []

for i in range(len(img)):
    
   
    for j in range(len(img[i])):
       listed_image.append(np.array([j,i,300*img[i][j]]))
        


samples = int(input("Dame el numero de puntos:  "))

dataset = []
xpoints = []
ypoints = []

for i in range(samples):
    index = np.random.randint(len(listed_image))
    dataset.append(listed_image[index])
    xpoints.append(listed_image[index][0])
    ypoints.append(listed_image[index][1])
    




treshold = 100
cond = 0
iteration = 0
while cond == 0:
    iteration+=1
    groups = []
    for i in dataset:
        if len(groups) == 0:
            groups.append([i])
        else:
            distances = []
            count = 0
            for j in groups:
                x = []
                y = []
                z = []
                for k in j:
                    x.append(k[0])
                    y.append(k[1])
                    z.append(k[2])
                
                group_media = np.array([np.mean(x),np.mean(y),np.mean(z)]) 
                
                distance = np.linalg.norm(i-group_media)
                
                if distance<treshold:
                    distances.append([distance,count])
                
                count+=1
                
            if(len(distances)>0):
                
                d = []
                for j in distances:
                    d.append(j)
                dmi = distances.index(min(d))
                
                groups[distances[dmi][1]].append(i)
            else:
                groups.append([i])
            
    print("Iteracion: "+str(iteration)+"   leng = "+str(len(groups)))
    if len(groups)==3:
        cond = 1
        print("\n\nValor final de umbral:  "+str(treshold))
        mediasx = []
        c = 0
        for i in groups:
            x = []
            
            for j in i:
                x.append(j[0])
            mediasx.append([np.mean(x),c])
            c+=1
            
            
        for i in range(len(mediasx)):
            for j in range(i,len(mediasx)):
                if(mediasx[j][0]>mediasx[i][0]):
                    aux = mediasx[i]
                    mediasx[i] = mediasx[j]
                    mediasx[j] = aux
        
        print(mediasx)
        ng = []    
        for i in range(len(groups)):
            ng.append(groups[mediasx[i][1]])
        
        groups = ng
    
    else:
        treshold+=2
        
                


colors = ["#ED2939","#FFFFFF","#002654",]

for i in range(len(groups)):
    s = groups[i]
    for j in s:
        plt.scatter(j[0],j[1],c=colors[i],edgecolors="black")

plt.legend()

    

io.imshow(img)

