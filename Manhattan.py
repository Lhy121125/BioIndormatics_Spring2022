import numpy as np

def LongestManhattan(Down,Right,n,m):
    """return the length of a longest path from source (0, 0) to sink (n, m)"""
    score = np.zeros([n+1, m+1])
    for j in range (1,n+1):
        score[j][0] = score[j-1][0] + Down[j-1][0]
    for i in range (1,m+1):
        score[0][i] = score[0][i-1] + Right[0][i-1]
    for j in range(1,n+1):
        for i in range(1,m+1):
            score[j][i] += max(score[j-1][i]+ Down[j-1][i],score[j][i-1]+Right[j][i-1])
    
    return score[n][m]

def read3(filename):
    """Read input data"""
    with open(filename, "r") as file:
        nm = file.readline().strip().split(" ")
        n = int(nm[0]) 
        m = int(nm[1])
        content = [line.strip() for line in file.readlines()]
        splitIndex = content.index("-")
        do = content[:splitIndex]
        ri = content[splitIndex+1:]
        #print(do)
        Down = []
        Right = []
        for str in do:
            Down.append(list(map(int, str.split(' '))))
        for str in ri:
            Right.append(list(map(int, str.split(' '))))
        return n,m,Down,Right

if __name__ == "__main__":
    n,m,Down,Right = read3("input_11.txt")
    
    print(LongestManhattan(Down,Right,n,m))
        