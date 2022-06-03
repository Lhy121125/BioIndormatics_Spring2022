import numpy as np
#received help from Trey

def EditDistance(v,w):
    """return the edit distance between two strings"""
    distances = np.zeros([len(v)+1, len(w)+1], dtype=int)

    for i in range(len(v)+1):
        for j in range(len(w)+1):
            if i == 0:
                distances[i][j] = j
            
            elif j == 0:
                distances[i][j] = i

            elif v[i-1] == w[j-1]:
                distances[i][j] = distances[i-1][j-1]
            
            elif v[i-1] != w[j-1]:
                distances[i][j] = 1 + min(distances[i-1][j],distances[i][j-1],distances[i-1][j-1])
            
    return distances[len(v)][len(w)]

def read6(filename):
    """Read input data"""
    with open(filename, "r") as file:
        v = file.readline().strip()
        w = file.readline().strip()
        return v,w

if __name__ == "__main__":
    v,w= read6("input_15.txt")
    #v = "PLEASANTLY"
    #w = "MEANLY"
    distance = EditDistance(v,w)
    print(distance)
