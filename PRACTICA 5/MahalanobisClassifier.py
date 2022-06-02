# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:02:13 2022

@author: argen
"""
import numpy as np
import matplotlib.pyplot as plt
from RandomColor import *

class MahalanobisClassifier:
    N = 0
    members = 0  
    classes = []
    medias = []
    colores = []
    cx = []
    cy = []
    D = []
    E = []
    Ei = []
    X = []
    
    def __init__(self, c):
        self.N = len(c)
        self.classes = c
        self.members = len(c[0])
        
        for i in range(0,self.N):
            self.cx.append([])
            self.cy.append([])
            self.colores.append(RandomColor.genHexCode())
            for j in range(self.members):
                self.cx[i].append(self.classes[i][j][0])
                self.cy[i].append(self.classes[i][j][1])
    
    def train(self):

            for i in range(self.N):
                self.X.append([])
                self.medias.append(np.array([np.mean(self.cx[i]),np.mean(self.cy[i])]))
                
            for i in range(self.N):
                
                for j in range(self.members):
                    self.X[i].append(self.classes[i][j]-self.medias[i])
            
            for i in range(self.N):
                Xaux = np.matrix(self.X[i])
                self.E.append(np.matmul(np.transpose(Xaux),Xaux)) 
                
                self.Ei.append(np.linalg.inv(self.E[i]))      
    def classify(self,v):
       
       D = []
       for i in range(self.N):
           D.append(np.matrix(v-self.medias[i]))
       distances = []
       for i in range(self.N):
           distances.append(np.matmul(np.matmul(D[i],self.Ei[i]),np.transpose(D[i])))
           
        
       
       
       return distances.index(min(distances)) + 1
    
        
    def plotClasesVec(self,v):
       
            
        for i in range(self.N):
            plt.scatter(self.cx[i],self.cy[i],color=self.colores[i],label="Clase "+str(i+1))
        plt.scatter(v[0],v[1], color="Black")
        plt.title("Clasificador Mahalanobis")
        
        plt.legend()
        plt.show()