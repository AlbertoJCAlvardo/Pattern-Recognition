# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:50:02 2022

@author: argen
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io,color
from random import shuffle



img = io.imread('llaves1.jpeg',as_gray=True)


listed_image = []
colores = []

for i in range(len(img)):
    for j in range(len(img[1])):
        if img[i][j] not in colores:
            colores.append(img[i][j])
    
dispersor = {}
inicial = -5000
for i in colores:
    
    dispersor[i] = inicial
    inicial += 50
    print(inicial)
    

for i in range(len(img)):
    
   
    for j in range(len(img[i])):
           listed_image.append(np.array([j,i,dispersor[img[i][j]]]))

samples = int(input("Dame el numero de puntos:  "))

dataset = []
xpoints = []
ypoints = []

for i in range(samples):
    index = np.random.randint(len(listed_image))
    dataset.append(listed_image[index])


K = int(input("Introduce K:  "))

groups = []
medias = []




converged = 0
epsilon = 0.025
counter = 0
iteraciones = 0
for i in range(K):
    groups.append([dataset[i]])
    medias.append(dataset[i])
    



while converged == 0:
    
    if(iteraciones == 0):
        medias_before = medias
    iteraciones +=1
    
    token = 0
    for i in dataset:
        distances = []
        
        
        for j in medias:
           
            distances.append(np.linalg.norm(i-j))
        
       
        mindex = distances.index(min(distances))
        groups[mindex].append(i)
   
    
    medias = []
    for s in range(len(groups)):
        x = []
        y = []
        z = []
        for k in groups[s]:
            x.append(k[0])
            y.append(k[1])
            z.append(k[2])
    
        medias.append(np.array([np.mean(x),np.mean(y),np.mean(z)]))
    
    
    md = []
    for i in range(len(medias)):
        md.append(np.linalg.norm(medias[i]-medias_before[i]))
   
        
    
    for i in md:
        if(i>epsilon):
            token = 1
            counter = 0
    
    if token == 0:
        counter+=1
        
                
    if counter == 50:
        
        print("Este programa convergio a las "+str(iteraciones)+" iteraciones")
        converged = 1
        mediasx = []
        c = 0
        for i in groups:
            x = []
            y = []
            for j in i:
                x.append(j[0])
                y.append(j[1])
            mediasx.append([np.mean([x,y]),c])
            c+=1
            
            
        for i in range(len(mediasx)):
            for j in range(i,len(mediasx)):
                if(mediasx[j][0]>mediasx[i][0]):
                    aux = mediasx[i]
                    mediasx[i] = mediasx[j]
                    mediasx[j] = aux
        
        
        ng = []    
        for i in range(len(groups)):
            ng.append(groups[mediasx[i][1]])
        groups = ng
        break        
    
    medias_before = medias
    shuffle(dataset)
    groups = []
    for i in range(K):
        groups.append([])
        



colors = ["#ED2939","#FFFFFF","#002654",]

for i in range(len(groups)):
    s = groups[i]
    for j in s:
        plt.scatter(j[0],j[1],c=colors[i],edgecolors="black")

plt.legend()

    

io.imshow(img)