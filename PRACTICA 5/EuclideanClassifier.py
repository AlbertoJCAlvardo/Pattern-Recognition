# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:34:23 2022

@author: argen
"""
import numpy as np
import matplotlib.pyplot as plt
from RandomColor import *

class EuclideanClassifier:
    N = 0
    classes = []
    medias = []
    colores = []
    def __init__(self, c):
        self.N = len(c)
        self.classes = c    
        for i in range(self.N):
            self.colores.append(RandomColor.genHexCode())
    def train(self):
        cx = []
        cy = []
        for i in range(0,self.N):
            cx.append([])
            cy.append([])
            for j in range(0,len(self.classes[i])):
                cx[i].append(self.classes[i][j][0])
                cy[i].append(self.classes[i][j][1])
            self.medias.append(np.array([np.mean(cx[i]), np.mean(cy[i])]))    
    
    def classify(self,v):
        distances = []
        for i in range(0,self.N):
            distances.append(np.linalg.norm(v-self.medias[i]))  
        
        return distances.index(min(distances)) + 1
    
    def plotClasesVec(self,v):
        cx = []
        cy = []
        for i in range(0,self.N):
            cx.append([])
            cy.append([])
            for j in range(0,len(self.classes[i])):
                cx[i].append(self.classes[i][j][0])
                cy[i].append(self.classes[i][j][1])
            
        for i in range(self.N):
            plt.scatter(cx[i],cy[i],color=self.colores[i],label="Clase "+str(i+1))
        plt.scatter(v[0],v[1], color="Black")
        plt.title("Clasificador Euclidiano")
        
        plt.legend()
        plt.show()


