import numpy as np
from Bio.Align import substitution_matrices
sub_mat = substitution_matrices.load("BLOSUM62") # or "PAM250"

def AffinePenalty(v,w):
    """The maximum alignment and score between v and w"""
    n = len(v)
    m = len(w)
    lower = np.zeros((n+1, m+1), dtype=int)
    middle = np.zeros((n+1, m+1), dtype=int)
    upper = np.zeros((n+1, m+1), dtype=int)
    Backtrack = np.zeros((n+1, m+1), dtype=int)

    # for i in range(1,n+1):
    #     lower[i][0] = -11 - (i-1) * 1
    #     middle[i][0] = -11 - (i-1) * 1
    #     upper[i][0] = -10 * 11

    # for j in range(1, m+1):
    #     upper[0][j] = -11 - (j-1) * 1
    #     middle[0][j] = -11 - (j-1) * 1
    #     lower[0][j] = -10 * 11
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            lower[i][j] = max([lower[i-1][j] - 1, middle[i-1][j] - 11])
            upper[i][j] = max([upper[i][j-1] - 1, middle[i][j-1] - 11])
            middle[i][j] = max(lower[i][j], middle[i-1][j-1] + sub_mat[v[i-1], w[j-1]], upper[i][j])
            
            if middle[i][j] == lower[i][j]:
                Backtrack[i][j] = 1
            elif middle[i][j] == upper[i][j]:
                Backtrack[i][j] = 2
            else:
                Backtrack[i][j] = 3

    maxScore = max(middle[n][m],lower[n][m],upper[n][m])
    i = n
    j = m
    vans = ""
    wans = ""

    while i>0 and j >0:
        if Backtrack[i][j] == 1:
            vans += v[i-1]
            wans += "-"
            i-=1
        elif Backtrack[i][j] == 2:
            vans += "-"
            wans += w[j-1]
            j -= 1
        else:
            vans += v[i-1]
            wans += w[j-1]
            i -= 1
            j -= 1

    
    return maxScore,vans[::-1],wans[::-1]

def read8(filename):
    """Read input data"""
    with open(filename, "r") as file:
        v = file.readline().strip()
        w = file.readline().strip()
        return v,w

if __name__ == "__main__":
    v,w= read8("input_18.txt")
    score, vans, wans = AffinePenalty(v,w)
    print(score)
    print(vans)
    print(wans)