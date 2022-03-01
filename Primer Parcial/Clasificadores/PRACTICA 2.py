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



centroides = [[0,-80],
              [100,0],
              [0,0],
              [-100,0]]


cex=[0,100,0,-100]
cey=[-80,0,0,0]

dispersion = [1,2,3,4]


    
cx = []
cy = [] 
media = []
colores = []

for i in range(4):
    
    cx.append(np.random.rand(1,100)+centroides[i][0] + dispersion[i]*np.random.rand(1,100))
    aux = cx[i]
    
    
    cy.append(np.random.rand(1,100)+ centroides[i][1]+ dispersion[i]*np.random.rand(1,100))
   
    
    media.append(np.array([np.mean(cx[i]),np.mean(cy[i])]))
    
    colores.append(randcolor())
    



loop = 1

while loop==1:

    for i in range(10): print("\n")
    
    sel = int(input("PRACTICA 2\n\n1)Clasificador por distancia euclidiana\n\n2)Clasificador por distancia Mahalanobis\nSu opcion:  "))

    x = float(input("Dame la coordenada en x del vector a clasificar:\n"))
    y = float(input("Dame la coordenada en y del vector a clasificar:\n"))
    
    
    v = np.array([x,y])
    print("\n\n\n\n\n\n\n\n\n\n")
    
    if(sel == 1):
        print("Clasificador por Distancia Euclideana")
        
        distancias = []
    
        for i in range(4):
            distancias.append(np.linalg.norm(media[i]-v))
    
    
    
    
    
    
    
        dmin = min(distancias)
    
        clase = distancias.index(dmin) + 1
    
        c = colores[clase-1]    
    
    
    
    
    
    
    
        for i in range(4):
            plt.scatter(cx[i],cy[i],color=colores[i],label="Clase "+str(i+1))
        
        
    
    
    
        plt.scatter(x,y,color="black")
    
        plt.xlabel("El vector pertenece a la clase "+str(clase),color="black")
    
    
    
        plt.title('Clasificador Por Distancia Euclideana')
    
        plt.legend()
        plt.show()
        
    elif(sel == 2):
        print("Clasificador por Distancia Mahalanobis")
        
        X1 = []    
        X2= []
        X3 = []
        X4 = []
        
        
        for i in range(100):
            X1.append([cx[0][0][i]-media[0][0], cy[0][0][i]-media[0][1]])
            X2.append([cx[1][0][i]-media[1][0], cy[1][0][i]-media[1][1]])
            X3.append([cx[2][0][i]-media[2][0], cy[2][0][i]-media[2][1]])
            X4.append([cx[3][0][i]-media[3][0], cy[3][0][i]-media[3][1]])
            
      
        X1 = np.matrix(X1)
        X2 = np.matrix(X2)
        X3 = np.matrix(X3)
        X4 = np.matrix(X4)
    
        E1 = np.matmul(np.transpose(X1),X1)
        E2 = np.matmul(np.transpose(X2),X2)
        E3 = np.matmul(np.transpose(X3),X3)
        E4 = np.matmul(np.transpose(X4),X4)
        
        D1 = np.matrix(v - np.array(media[0]))
        D2 = np.matrix(v - np.array(media[1]))
        D3 = np.matrix(v - np.array(media[2]))
        D4 = np.matrix(v - np.array(media[3]))
        
        d = []
        d.append(np.matmul(np.matmul(D1,np.linalg.inv(E1)),np.transpose(D1)))
        d.append(np.matmul(np.matmul(D2,np.linalg.inv(E2)),np.transpose(D2)))
        d.append(np.matmul(np.matmul(D3,np.linalg.inv(E3)),np.transpose(D3)))
        d.append(np.matmul(np.matmul(D4,np.linalg.inv(E4)),np.transpose(D4)))
        
        dmin = min(d)
        clase = d.index(dmin) + 1
        
        c = colores[clase-1]    
    
    
    
        for i in range(4):
            plt.scatter(cx[i],cy[i],color=colores[i],label="Clase "+str(i+1))
        
        
    
    
    
        plt.scatter(x,y,color="black")
    
        plt.xlabel("El vector pertenece a la clase "+str(clase),color="black")
    
    
    
        plt.title('Clasificador Por Distancia Mahalanobis')
    
        plt.legend()
        plt.show()
        
        
        
        
    else:
        print("Error")
        
    loop = int(input("\n\nDesea clasificar otro vector?\n\n1)Si\t0)No\nSu opcion: "))
    
    
