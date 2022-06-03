import numpy as np

def FittingAlignment(v,w):
    """The maximum score and the alignment of two sequences"""
    n = len(v)
    m = len(w)
    scores = np.zeros([n+1, m+1], dtype=int)
    Backtrack = np.full((n+1,m+1),"0")

    for i in range(n+1):
        scores[i][0] = 0
        Backtrack[i][0] = "↓"

    for j in range(m+1):
        scores[0][j] = (-1) * j
        Backtrack[0][j] = "→"

   
    for i in range(1,n+1):
        for j in range(1,m+1):
            scores[i][j] = max(scores[i-1][j-1] + 1 if v[i-1] == w[j-1] else scores[i-1][j-1] -1, scores[i][j-1]-1, scores[i-1][j]-1)
            #down
            if (scores[i][j] == scores[i-1][j]-1):
                Backtrack[i][j] = "↓"
            #right
            elif (scores[i][j] == scores[i][j-1]-1):
                Backtrack[i][j] = "→"
            #diagonal
            else:
                Backtrack[i][j] = "↘"
    
    
    j = m
    maxScore = -10000
    maxIndex = 0
    for i in range(n+1):
        if scores[i][j] > maxScore:
            maxScore = scores[i][j]
            maxIndex = i
    i = maxIndex

    
    vans, wans = v[:i], w[:j]

    while i>0 and j >0:
        if Backtrack[i][j] == "↓":
            wans = wans[:j] + "-" + wans[j:]
            i -= 1
        elif Backtrack[i][j] == "→":
            vans = vans[:i] + "-" + vans[i:]
            j -= 1
        elif Backtrack[i][j] == "↘":
            i -= 1
            j -= 1

    vans = vans[i:]

    return maxScore, vans, wans


def read7(filename):
    """Read input data"""
    with open(filename, "r") as file:
        v = file.readline().strip()
        w = file.readline().strip()
        return v,w

if __name__ == "__main__":
    v,w= read7("input_17.txt")
    #v = "GTAGGCTTAAGGTTA"
    #w = "TAGATA"
    score, vans, wans = FittingAlignment(v,w)
    print(score)
    print(vans)
    print(wans)