import numpy as np
from Bio.Align import substitution_matrices
sub_mat = substitution_matrices.load("PAM250")

def LocalAlginment(v,w):
    """return the highest-scoring local alignment between two strings"""
    n = len(v)
    m = len(w)
    scores = np.zeros([n+1, m+1], dtype=int)

    for i in range(n+1):
        scores[i][0] = (-5) * i

    for j in range(m+1):
        scores[0][j] = (-5) * j
    
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            scores[i][j] = max(0,scores[i-1][j-1] + sub_mat[(v[i-1],w[j-1])], scores[i-1][j]-5, scores[i][j-1]-5)

    #print(scores)
    maxScore = 0

    #find the maximum score
    for a in range(n+1):
        for b in range(m+1):
            if scores[a][b] > maxScore:
                maxScore = scores[a][b]
                i = a
                j = b


    #Find the optimal sequence
    vans = []
    wans = []

    while (i >= 0 and j >= 0):
        #Diagonal
        maxi = scores[i][j] - sub_mat[(v[i-1],w[j-1])]
        if maxi == scores[i-1][j-1]:
            vans.append(v[i-1])
            wans.append(w[j-1])
            i -= 1
            j -= 1
        else:
            maxi = max(scores[i-1][j],scores[i][j-1])
            if maxi == scores[i-1][j]:
                vans.append(v[i-1])
                wans.append("-")
                i -= 1
            else:
                vans.append("-")
                wans.append(w[j-1])
                j -= 1
        if maxi == 0:
            break
    
    return maxScore, "".join(vans)[::-1], "".join(wans)[::-1]

def read5(filename):
    """Read input data"""
    with open(filename, "r") as file:
        v = file.readline().strip()
        w = file.readline().strip()
        return v,w

if __name__ == "__main__":
    v,w= read5("input_13.txt")
    #v = "MEANLY"
    #w = "PENALTY"
    score, vans, wans = LocalAlginment(v,w)
    print(score)
    print(vans)
    print(wans)