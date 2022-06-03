import numpy as np
#received help from Ansen
from Bio.Align import substitution_matrices
sub_mat = substitution_matrices.load("BLOSUM62") # or "PAM250"


def GlobalAlginment(v,w):
    """return the highest-scoring alignment between two strings using a scoring matrix"""
    n = len(v)
    m = len(w)
    scores = np.zeros([n+1, m+1], dtype=int)
    Backtrack = np.full((n+1,m+1),"0")

    for i in range(n+1):
        scores[i][0] = (-5) * i
        Backtrack[i][0] = "↓"

    for j in range(m+1):
        scores[0][j] = (-5) * j
        Backtrack[0][j] = "→"
    
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            scores[i][j] = max(scores[i-1][j-1] + sub_mat[(v[i-1],w[j-1])], scores[i-1][j]-5, scores[i][j-1]-5)
            #down
            if (scores[i][j] == scores[i-1][j]-5):
                Backtrack[i][j] = "↓"
            #right
            elif (scores[i][j] == scores[i][j-1]-5):
                Backtrack[i][j] = "→"
            #diagonal
            else:
                Backtrack[i][j] = "↘"

    maxScore = scores[n][m]
    #print(Backtrack)
    #print("-------------------------")
    #print(scores)

    #Find the optimal sequence
    vans = []
    wans = []
    i = n
    j = m

    while (i >= 0 and j >= 0):
            if Backtrack[i][j] == "↘":
                vans.append(v[i-1])
                wans.append(w[j-1])
                i = i-1
                j = j-1
            elif Backtrack[i][j] == "↓":
                vans.append(v[i-1])
                wans.append("-")
                i -= 1
            elif Backtrack[i][j] == "→":
                vans.append("-")
                wans.append(w[j-1])
                j -= 1
    vans = vans[:-1]
    wans = wans[:-1]
    
    return maxScore, "".join(vans)[::-1], "".join(wans)[::-1]

def read4(filename):
    """Read input data"""
    with open(filename, "r") as file:
        v = file.readline().strip()
        w = file.readline().strip()
        return v,w

if __name__ == "__main__":
    v,w= read4("input_12.txt")
    #v = "PLEASANTLY"
    #w = "MEANLY"
    score, vans, wans = GlobalAlginment(v,w)
    print(score)
    print(vans)
    print(wans)