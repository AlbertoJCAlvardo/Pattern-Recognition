


import numpy  as np
import matplotlib.pyplot as plt


def randcolor():
    r = hex(np.random.randint(0,255))
    g = hex(np.random.randint(0,255))
    b = hex(np.random.randint(0,255))
        
    
    sr=""
    sg=""
    sb=""
    
    for i in range(2,len(r)):
        if(len(r)<4):
            sr += "0"
        sr += str(r[i])
    for i in range(2,len(g)):
        if(len(g)<4):
            sg += "0"
        sg += str(g[i])
    for i in range(2,len(b)):
        if(len(b)<4):
            sb += "0"
        sb += str(b[i])
        
        
        
        
    f = "#"+sr+sg+sb
    
    return f



N = int(input("Inserte el número de clases:  "))

centroides = []
cex=[]
cey=[]
dispersion = []


for k in range(N):
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    x = float(input("Coordenada en x del centroide de la clase "+str(k+1)+":   "))
    y = float(input("Coordenada en y del centroide de la clase "+str(k+1)+":   "))
    dispersion.append(float(input("Dispersión maxima entre miembros de la clase "+str(k+1)+":    ")))
    
    centroides.append([x,y])
    cex.append(x)
    cey.append(y)

    
cx = []
cy = [] 
media = []
colores = []

for i in range(N):
    
    cx.append(np.random.rand(1,100)+centroides[i][0] + dispersion[i]*np.random.rand(1,100))
    aux = cx[i]
    
    
    cy.append(np.random.rand(1,100)+ centroides[i][1]+ dispersion[i]*np.random.rand(1,100))
   
    
    media.append(np.array([np.mean(cx[i]),np.mean(cy[i])]))
    
    colores.append(randcolor())
    



x = float(input("Dame la coordenada en x del vector a clasificar:\n"))
y = float(input("Dame la coordenada en y del vector a clasificar:\n"))

v = np.array([x,y])

distancias = []

for i in range(N):
    distancias.append(np.linalg.norm(media[i]-v))







dmin = min(distancias)

clase = distancias.index(dmin) + 1

c = colores[clase-1]







for i in range(N):
    plt.scatter(cx[i],cy[i],color=colores[i],label="Clase "+str(i+1))
    
    



plt.scatter(x,y,color=c)

plt.xlabel("El vector pertenece a la clase "+str(clase),color="black")



plt.title('Clasificador')

plt.legend()
plt.show()
