# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:29:43 2022

@author: argen
"""

import numpy as np
import matplotlib.pyplot as plt
from RandomColor import *
class KNNClassifier:
    
    N = 0
    K = 0
    members = 0
    classes = 0
    cx = []
    cy = []
    colores = []
    
    def __init__(self,c,k):
        self.classes = c
        self.N = len(c)
        self.members = len(c[0])
        self.K = k
        for i in range(0,self.N):
            self.cx.append([])
            self.cy.append([])
            self.colores.append(RandomColor.genHexCode())
            for j in range(0,len(self.classes[i])):
                self.cx[i].append(self.classes[i][j][0])
                self.cy[i].append(self.classes[i][j][1])
    
    
    def classify(self,v):
        d = []
        for i in range(self.N):
            
            for j in range(self.members):
                    d.append([np.linalg.norm(v-self.classes[i][j]),i+1])
                
        for i in range(len(d)):
           for j in range(i):
               if d[i][0] < d[j][0]:
                   aux = d[j]
                   d[j] = d[i]
                   d[i] = aux
                

                
        contadores = []
        for i in range(self.N):
            contadores.append(0)
        for i in d:
            if self.K in contadores:
                break
            contadores[i[1]-1] += 1
            
        return contadores.index(self.K) + 1
        
        