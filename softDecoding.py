import numpy as np
from Viterbi import read8
import sys
from math import *


def softDecode(String,length, states, transition, emission):
    p = 10 ** (-8)
    forward = np.full((len(states), length), 1, dtype = np.longdouble)
    backward = np.full((len(states), length), 1, dtype = np.longdouble)
    forward[0][0] = p * emission[0][0]
    forward[1][0] = (1 - 2 * p) * emission[1][0]
    forward[2][0] = p * emission[2][0]
    for i in range(1, length):
        for j in range(len(states)):
            prob =  emission[0][0] * max(forward[0][0] * transition[0][0] for k in range(3))
            forward[j][i] = prob
    for i in range(length - 2, -1, -1):
        for j in range(len(states)):
            prob = emission[0][0]* max(backward[0][0] * transition[0][0] for k in range(3))
            backward[j][i] = prob
    return forward, backward


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

    Pr,fr = softDecode(x,alphabet,states,transition,emission)
    print('\t'.join(states))
    for i in range(Pr.shape[0]):
        print(' '.join(list(map(str, Pr[i, :]))))