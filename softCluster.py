import math
from LLoyd import distance

def eStep(data, beta, centers):
    eMatrix = [[0]*len(data) for x in range(len(centers))]
    size = len(centers)

    for i in range(len(data)):
        sum = 0.0
        for j in range(size):
            dist = distance(centers[j], data[i])
            eMatrix[j][i] = math.exp(-beta * dist)
            sum += eMatrix[j][i]
        for j in range(size):
            eMatrix[j][i] /= sum
            
    return eMatrix

def mStep(data, eMatrix, m):
    centers = []
    
    for i in range(len(eMatrix)):
        center = []
        for j in range(m):
            product = 0.0
            divide = 0.0
            for k in range(len(data)):
                product += data[k][j] * eMatrix[i][k]
                divide += eMatrix[i][k]
            center.append(product/divide)
        centers.append(center)
        
    return centers

def soft(data, k, m, beta):
    centers = [ data[x] for x in range(k) ]
    
    for i in range(100):
        eMatrix = eStep(data, beta, centers)
        centers = mStep(data, eMatrix, m)
        
    return centers

def read24(filename):
    with open(filename, "r") as file:
        km = file.readline().split()
        k = int(km[0])
        m = int(km[1])
        beta = float(file.readline())
        points = [[float(i) for i in line.split()] for line in file.readlines()]
        #print(points)
        return k,m,beta,points

if __name__ == "__main__":
    k,m,beta,points = read24("debug24.txt")
    centers = soft(points,k,m,beta)

    for center in centers:
        print(" ".join(map(str,center)))
    
