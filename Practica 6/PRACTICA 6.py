# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:47:33 2022

@author: Alberto J.C. Alvarado
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def hardlims(n):
    if(n>=0):
        return 1
    else:
        return 0





"""
               Conjunto vector-clase
               (x,y,z):clase
"""      




clases = { 
            (0,0,0):0,
            (0,0,1):1,
            (0,1,0):1,
            (0,1,1):1,
            (1,0,0):0,
            (1,0,1):0,
            (1,1,0):0,
            (1,1,1):1
          }

x1 = []
y1 = []
z1 = []
x2 = []
y2 = []
z2 = []

for i in clases:
    if clases[i] == 0:
        x1.append(i[0])
        y1.append(i[1])
        z1.append(i[2])
    else:
        x2.append(i[0])
        y2.append(i[1])
        z2.append(i[2])


"""" Generamos un vector con tres componentes aleatorias
     entre 1 y 0 y un bias aleatorio

"""

w = np.array((np.random.rand(),np.random.rand(),np.random.rand()))     
b = np.random.rand()


print("w(0) = "+str(w)+"   b(0) = "+str(b))

epoca = 1
iteracion = 1

validacion = 0


alpha = 0.5
t = 0
errores = []
epocas = []
"""Entrenando el perceptron con las reglas"""

while validacion == 0:
    print("\n\n--------------------------------------")
    print("   Epoca "+str(epoca))
    k = 0
    iteracion = 0
    et = 0
    for i in clases:
        iteracion += 1
        t += 1
        a = np.dot(np.array(i),w) + b
        s = hardlims(a)
            
        e = clases[i] - s
        et += abs(e)
        if e == 0:
            k += 1
            
        wa = w
        ba = b
        b = b + e
        w = w + e*alpha*np.array(i)
        
        print("\n\n\tIteracion "+str(iteracion))
        print("\t\t"+str(np.array(i))+" "+str(w)+" + "+str(b)+" = "+str(a))
        print("\t\t s = "+str(s)+", e = "+str(e))
        print("\n\t\t w("+str(t)+") = "+str(wa)+" + ("+str(e)+")("+str(alpha)+")"+str(np.array(i))+" = "+str(w))
        print("\t\t b("+str(t)+") = "+str(ba)+" + "+str(e)+" = "+str(b))
    
    if k == len(clases):
        validacion = 1
    epocas.append(epoca)
    errores.append(et)
    epoca += 1    
        
print("\n\n\n Finalmente   w = "+str(w)+",    b = "+str(b))


fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')


ax1.scatter(x1,y1,z1, color="blue")
ax1.scatter(x2,y2,z2, color="red")

xx, yy = np.meshgrid(range(2),range(2)) 
xx = xx
yy = yy
z = (-w[0]*xx - w[1]*yy - b)*1./w[2]

ax1.plot_surface(xx,yy,z, alpha=0.8,color="green")