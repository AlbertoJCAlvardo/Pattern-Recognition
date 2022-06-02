# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 23:30:47 2022

@author: argen
"""

import matplotlib.pyplot as plt
import gc


from EuclideanClassifier import EuclideanClassifier as EC
from MahalanobisClassifier import MahalanobisClassifier as MC
from BayesianClassifier import BayesianClassifier as BC
from KNNClassifier import KNNClassifier as KC
from ClassGenerator import ClassGenerator as CG
from ConfussionMatrix import ConfussionMatrix 
from RandomColor import RandomColor as RC




N = int(input("Inserte el número de clases:  "))
members = int(input("Inserte el numero de miembros de clase: "))


centroides = []
dispersion = []


for k in range(N):
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    x = float(input("Coordenada en x del centroide de la clase "+str(k+1)+":   "))
    y = float(input("Coordenada en y del centroide de la clase "+str(k+1)+":   "))
    dispersion.append(abs(float(input("Dispersión maxima entre miembros de la clase "+str(k+1)+":    "))))
    
    centroides.append([x,y])
cg = CG()

classes = cg.genC(centroides,dispersion,members)

train_switch = 0
loop = 1



cv_train = []
cv_test = []
hio_train = []
hio_test = []

CM = ConfussionMatrix()


for i in range(N):    
    cv_train.append([])
    cv_test.append([])
    for j in range(members//2):
        cv_train[i].append(classes[i][j])
        cv_test[i].append(classes[i][j+members//2])


for i in range(N):
    hio_train.append([])
    for k in range(members-1):
        hio_train[i].append(classes[i][j])
    hio_test.append(classes[i][members-1])


ere = EC(classes)
ecv = EC(cv_train)
ehio = EC(hio_train)


mre = MC(classes)
mcv = MC(cv_train)
mhio = MC(hio_train)

bre = BC(classes)
bcv = BC(cv_train)
bhio = BC(hio_train)

ere.train()
ecv.train()
ehio.train()
        
        
mre.train()
mcv.train()
mhio.train()
        
bre.train()
bcv.train()
bhio.train()



rendimientos = []
textos = ["Restitution", "Cross validation", "Hold in One"]

colores_clases = []



colores_lineas = ["Black","Yellow","Red"]

t_rendimientos = ""


while loop == 1:
    sel = int(input("PRACTICA 5: Rendimiento de modelos n\n1)Distancia euclidiana\n\n2)Distancia Mahalanobis\n\n3)Por Criterio Bayesiano\n\n4)KNN\n\n\nSu opcion:  "))    
  
    
    if(sel == 1):
        
        t_rendimientos = "Rendimientos del Clasificador Euclidiano"

        print("\n\n\n\n\n\n\n\n")
        print("Clasificador Euclidiano")
        #Restitution
        
        rendimientos = []
        
        cmr = []
        for i in range(N):
            cmr.append([])
            for s in range(N):
                cmr[i].append(0)
                
            for j in range(members):
                
                clase = ere.classify(classes[i][j])
                cmr[i][clase-1] += 1
        print("\n\n\n\n\n\n")
        print("Restitution")
        
        CM.printConfussion(cmr,members,0)
        
        rendimientos.append(CM.getPerformance(cmr,members,0))
        
        
        
        #Cross Validation
        
        cmc = []
        for i in range(N):
            cmc.append([])
            for s in range(N):
                cmc[i].append(0)
                
            for j in range(members//2):
                
                clase = ecv.classify(cv_test[i][j])
                cmc[i][clase-1] += 1
        print("\n\n\n\n\n\n")
        print("Cross Validation")
        
        CM.printConfussion(cmc,members//2,0)
        
        rendimientos.append(CM.getPerformance(cmc,members//2,1))
        
        #Hold in One
        
        
        chio = []
        
        for i in range(N):
            chio.append([])
            for s in range(N):
                chio[i].append(0)
                
            clase = ehio.classify(hio_test[i])
            chio[i][clase-1] += 1
        
        print("\n\n\n\n\n\n")
        print("Hold In One")
        
        CM.printConfussion(chio,1,2)
        
        rendimientos.append(CM.getPerformance(chio,1,2))
    
    if(sel == 2):
        
        t_rendimientos = "Rendimientos del Clasificador Mahalanobis"

        print("\n\n\n\n\n\n\n\n")
        print("Clasificador Mahalanobis")
        #Restitution
        
        rendimientos = []
        
        cmr = []
        for i in range(N):
            cmr.append([])
            for s in range(N):
                cmr[i].append(0)
                
            for j in range(members):
                
                clase = mre.classify(classes[i][j])
                cmr[i][clase-1] += 1
        print("\n\n\n\n\n\n")
        print("Restitution")
        
        CM.printConfussion(cmr,members,0)
        
        rendimientos.append(CM.getPerformance(cmr,members,0))
        
        
        
        #Cross Validation
        
        cmc = []
        for i in range(N):
            cmc.append([])
            for s in range(N):
                cmc[i].append(0)
                
            for j in range(members//2):
                
                clase = mcv.classify(cv_test[i][j])
                cmc[i][clase-1] += 1
        print("\n\n\n\n\n\n")
        print("Cross Validation")
        
        CM.printConfussion(cmc,members//2,0)
        
        rendimientos.append(CM.getPerformance(cmc,members//2,1))
        
        #Hold in One
        
        
        chio = []
        
        for i in range(N):
            chio.append([])
            for s in range(N):
                chio[i].append(0)
                
            clase = mhio.classify(hio_test[i])
            chio[i][clase-1] += 1
        
        print("\n\n\n\n\n\n")
        print("Hold In One")
        
        CM.printConfussion(chio,1,2)
        
        rendimientos.append(CM.getPerformance(chio,1,2))


    if(sel == 3):
        
        t_rendimientos = "Rendimientos del Clasificador Bayesiano"

        print("\n\n\n\n\n\n\n\n")
        print("Clasificador Bayesiano")
        #Restitution
        
        rendimientos = []
        
        cmr = []
        for i in range(N):
            cmr.append([])
            for s in range(N):
                cmr[i].append(0)
                
            for j in range(members):
                
                clase = bre.classify(classes[i][j])
                cmr[i][clase-1] += 1
        print("\n\n\n\n\n\n")
        print("Restitution")
        
        CM.printConfussion(cmr,members,0)
        
        rendimientos.append(CM.getPerformance(cmr,members,0))
        
        
        
        #Cross Validation
        
        cmc = []
        for i in range(N):
            cmc.append([])
            for s in range(N):
                cmc[i].append(0)
                
            for j in range(members//2):
                
                clase = bcv.classify(cv_test[i][j])
                cmc[i][clase-1] += 1
        print("\n\n\n\n\n\n")
        print("Cross Validation")
        
        CM.printConfussion(cmc,members//2,0)
        
        rendimientos.append(CM.getPerformance(cmc,members//2,1))
        
        #Hold in One
        
        
        chio = []
        
        for i in range(N):
            chio.append([])
            for s in range(N):
                chio[i].append(0)
                
            clase = bhio.classify(hio_test[i])
            chio[i][clase-1] += 1
        
        print("\n\n\n\n\n\n")
        print("Hold In One")
        
        CM.printConfussion(chio,1,2)
        
        rendimientos.append(CM.getPerformance(chio,1,2))
    
    if(sel == 4):
        
        t_rendimientos = "Rendimientos del Clasificador KNN"

        print("\n\n\n\n\n\n\n\n")
        print("Clasificador KNN")
        
        K = int(input("Inserte K impar:  "))
        
        kre = KC(classes,K)
        kcv = KC(cv_train,K)
        khio = KC(hio_train,K)
        
        #Restitution
        
        rendimientos = []
        
        cmr = []
        for i in range(N):
            cmr.append([])
            for s in range(N):
                cmr[i].append(0)
                
            for j in range(members):
                
                clase = kre.classify(classes[i][j])
                cmr[i][clase-1] += 1
        print("\n\n\n\n\n\n")
        print("Restitution")
        
        CM.printConfussion(cmr,members,0)
        
        rendimientos.append(CM.getPerformance(cmr,members,0))
        
        
        
        #Cross Validation
        
        cmc = []
        for i in range(N):
            cmc.append([])
            for s in range(N):
                cmc[i].append(0)
                
            for j in range(members//2):
                
                clase = kcv.classify(cv_test[i][j])
                cmc[i][clase-1] += 1
        print("\n\n\n\n\n\n")
        print("Cross Validation")
        
        CM.printConfussion(cmc,members//2,0)
        
        rendimientos.append(CM.getPerformance(cmc,members//2,1))
        
        #Hold in One
        
        
        chio = []
        
        for i in range(N):
            chio.append([])
            for s in range(N):
                chio[i].append(0)
                
            clase = khio.classify(hio_test[i])
            chio[i][clase-1] += 1
        
        print("\n\n\n\n\n\n")
        print("Hold In One")
        
        CM.printConfussion(chio,1,2)
        
        rendimientos.append(CM.getPerformance(chio,1,2))
        
    
    for i in range(len(rendimientos)):
        
        plt.plot(rendimientos[i][0],rendimientos[i][1],label=textos[i],color=colores_lineas[i])
    
    plt.title(t_rendimientos)
    plt.legend()
    
    plt.show()
    
    
    cg.plotClasses()   
    gc.collect()
    
        
    loop = int(input("Desea probar el rendimiento de otro clasificador?  1)Si  0)No"))




    