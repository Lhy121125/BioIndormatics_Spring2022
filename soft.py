import numpy as np
from Viterbi import read8
import sys
from math import *

def softDecode(x, alphabet,states,transition, emission):
    """Return The probability Pr(πi = k|x) that the HMM was in state k at step i (for each state k and each step i)."""
    n = len(x)
    m = len(states)
    forward = np.full((n, m), 1, dtype=np.longdouble)
    backward = np.full((n, m), 1, dtype=np.longdouble)
    forward[0, :] = emission[:, alphabet.index(x[0])]/m
    backward[n - 1, :] = 1

    for i in range(1, n):
        for j in range(m):
            forward[i, j] = sum(forward[i - 1, :] * transition[:, j] * emission[j, alphabet.index(x[i])])

    sink = sum(forward[n-1])

    for i in range(n - 2, -1, -1):
        for j in range(m):
            backward[i, j] = sum(backward[i + 1, :] * transition[j, :] * emission[:, alphabet.index(x[i + 1])])

    Pr = np.zeros((n, m), dtype = float)
    for i in range(n):
        for k in range(m):
            Pr[i, k] = forward[i][k]*backward[i][k]/sink

    return Pr

def read22(filename):
    """"read the input"""
    with open(filename, "r") as file:
        data = file.read().strip().split()
        x = data[0]
        rest = [i for i in range(len(data)) if '--------' == data[i]]
        alphabet = data[rest[0]+1:rest[1]]
        states = data[rest[1]+1:rest[2]]
        transition = np.zeros((len(states), len(states)), dtype = float)
        emission = np.zeros((len(states), len(alphabet)), dtype = float)
        for i in range(len(states)):
            transition[i, :] = [float(d) for d in data[rest[2]+len(states)+2+i*(len(states)+1):rest[2]+len(states)+1+(i+1)*(len(states)+1)]]
            emission[i, :] = [float(d) for d in data[rest[3]+len(alphabet)+2+i*(len(alphabet)+1):rest[3]+len(alphabet)+1+(i+1)*(len(alphabet)+1)]]
        return x, transition, emission, alphabet, states

if __name__ == "__main__":
    x,transition,emission,alphabet,states = read22("debug22.txt")

    Pr = softDecode(x,alphabet,states,transition,emission)
    print('\t'.join(states))
    for i in range(Pr.shape[0]):
        print(' '.join(list(map(str, Pr[i, :]))))