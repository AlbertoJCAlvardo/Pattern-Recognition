# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:56:07 2022

@author: argen
"""

import numpy as np
import matplotlib.pyplot as plt
from RandomColor import RandomColor as RC

class ClassGenerator:
    a = 0
    N = 0
    cy = []
    cx = []
    clases = []
    members = 0
    colores = []
    def __init__(self):
        print("Generador de Clases Creado")
    def genC(self,centroides,dispersion,members):
        self.classes = []
        self.members = members
        self.N = len(centroides)
        
        mux = []
        muy = []
        
        for i in range(members):
            mux.append((pow(-1,np.random.randint(2))))
            muy.append((pow(-1,np.random.randint(2))))
        
        mux = np.array(mux)
        muy = np.array(muy)
        
       
        
        for i in range(len(centroides)):
            self.classes.append([])
            
            self.colores.append(RC.genHexCode())
            self.cx = np.random.rand(1,members)+centroides[i][0] + mux*dispersion[i]*np.random.rand(1,members)
            self.cy =  np.random.rand(1,members)+centroides[i][1] +muy*dispersion[i]*np.random.rand(1,members)
            for j in range(len(self.cx[0])):
                self.classes[i].append(np.array([self.cx[0][j],self.cy[0][j]]))
        
        self.cx = []
        self.cy = []
        
        for i in range(0,self.N):
            self.cx.append([])
            self.cy.append([])
            
            for j in range(0,len(self.classes[i])):
                self.cx[i].append(self.classes[i][j][0])
                self.cy[i].append(self.classes[i][j][1])
        return self.classes
    
    def plotClasses(self):
        
        for i in range(self.N):
            plt.scatter(self.cx[i],self.cy[i],label="Clase "+str(i+1),color =self.colores[i])
           
        plt.legend()
        plt.show()