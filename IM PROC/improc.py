import numpy as np
from skimage import io,color


img = io.imread('francia.png',as_gray=True)
dimensions = 0
print(dimensions)

k = []
r = []
s=0

for i in range(len(img)):
    r.append([])
    k.append([])
    for j in range(len(img[i])):
        a = []
        a.append((img[i][j]+12)%22)
        r[i].append(np.array(img[i][j]))
        k[i].append(np.array(a))
        
k = np.array(k)
r = np.array(r)



n = io.imsave("neo1.png",r)
s = io.imsave("neo.png",k)

io.imshow(img)