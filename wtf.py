import numpy as np
from Viterbi import read8
import sys
from math import *

def softDecode(x, alphabet,states,transition, emission):
    n = len(x)
    l = transition.shape[0]
    x2ind = {alphabet[i]:i for i in range(len(alphabet))}
    xList = [x2ind[x[i]] for i in range(len(x))]
    forward = [[0 for _ in range(l)] for __ in range(n)]
    backward = [[0 for _ in range(l)] for __ in range(n)]
    for k in range(l):
        forward[0][k] = emission[k, xList[0]]/l
    for i in range(1, n):
        for k in range(l):
            forward[i][k] = sum([forward[i-1][kpre]*transition[kpre, k]*emission[k, xList[i]] for kpre in range(l)])
    fsink = sum(forward[n-1])

    for k in range(l):
        backward[n-1][k] = 1
    for i in range(n-2, -1, -1):
        for k in range(l):
            backward[i][k] = sum([backward[i+1][kpre]*transition[k, kpre]*emission[kpre, xList[i+1]] for kpre in range(l)])
        
    Pr = np.zeros((n, l), dtype = float)
    for i in range(n):
        for k in range(l):
            Pr[i, k] = forward[i][k]*backward[i][k]/fsink

    return Pr

def readFromFile():
    f = open('debug22.txt', 'r')
    data = f.read().strip().split()
    x = data[0]
    ind = [i for i in range(len(data)) if '--------' == data[i]]
    alphabet = data[ind[0]+1:ind[1]]
    states = data[ind[1]+1:ind[2]]
    transition = np.zeros((len(states), len(states)), dtype = float)
    emission = np.zeros((len(states), len(alphabet)), dtype = float)
    for i in range(len(states)):
        transition[i, :] = [float(d) for d in data[ind[2]+len(states)+2+i*(len(states)+1):ind[2]+len(states)+1+(i+1)*(len(states)+1)]]
        emission[i, :] = [float(d) for d in data[ind[3]+len(alphabet)+2+i*(len(alphabet)+1):ind[3]+len(alphabet)+1+(i+1)*(len(alphabet)+1)]]
    return x, transition, emission, alphabet, states

if __name__ == "__main__":
    x,transition,emission,alphabet,states = readFromFile()
    print(emission)

    Pr = softDecode(x,alphabet,states,transition,emission)
    print('\t'.join(states))
    for i in range(Pr.shape[0]):
        print(' '.join(list(map(str, Pr[i, :]))))