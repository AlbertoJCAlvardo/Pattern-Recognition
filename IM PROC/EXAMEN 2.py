

import numpy as np
import matplotlib.pyplot as plt
from skimage import io,color
from random import shuffle
from RandomColor import *



img = io.imread('figures1.png',as_gray=True)

listed_image = []
colores = []

for i in range(len(img)):
    for j in range(len(img[1])):
        if img[i][j] not in colores:
            colores.append(img[i][j])
    
dispersor = {}
inicial = -1000
for i in colores:
    
    dispersor[i] = inicial
    inicial += 5000
    
print(dispersor)
for i in range(len(img)):
    
   
    for j in range(len(img[i])):
       if img[i][j] != 1.0:
           listed_image.append(np.array([j,i,dispersor[img[i][j]]]))
       



samples = 300

dataset = []

i = 0

while i < samples:
    
    index = np.random.randint(len(listed_image))
    
    dataset.append(listed_image[index])
    i += 1
    
    
    



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
    
    if(iteraciones<6):
        for i in range(len(medias)):
            color = RandomColor.genHexCode()
            plt.scatter(medias[i][0],medias[i][1],label="Centroide de la clase "+str(i+1),c=color)
                    
        plt.title("Centroides en la iteracion "+str(10*iteraciones))
        plt.legend()
        plt.show()
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
        for i in range(len(medias)):
            color = RandomColor.genHexCode()
            plt.scatter(medias[i][0],medias[i][1],label="Centroide de la clase "+str(i+1),c=color)
                    
        plt.title("Centroides en la iteracion "+str(iteraciones))
        plt.legend()
        plt.show()
        
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
        



colors = ["#0000FF","#FF0000","#00FF00",]

for i in range(len(groups)):
    s = groups[i]
    for j in s:
        plt.scatter(j[0],j[1],c=colors[i],edgecolors="black")

plt.legend()

    

io.imshow(img)