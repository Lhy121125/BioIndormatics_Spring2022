import numpy as np
import rosalind2B
import rosalind2C
import math
"""Received Help From Trey"""


def formProfile(motifs):
    """return the profile of given motifs"""
    countProfile = np.full((4,len(motifs[0])), 0, dtype=np.float_)
    probProfile = np.full((4,len(motifs[0])), 0, dtype=np.float_)
    #print(motifs)
    for i in range(len(motifs)):
        for j in range(len(motifs[0])):
            if motifs[i][j] == "A":
                countProfile[0][j] += 1
            if motifs[i][j] == "C":
                countProfile[1][j] += 1
            if motifs[i][j] == "G":
                countProfile[2][j] += 1
            if motifs[i][j] == "T":
                countProfile[3][j] += 1

    for i in range(len(countProfile)):
        for j in range(len(countProfile[0])):
            probProfile[i][j] = countProfile[i][j]/len(motifs)
    
    return probProfile


def getScore(motifs):
    """Returns the score of the motifs"""
    score = 0
    for i in range(len(motifs[0])):
        motif = ''.join([motifs[j][i] for j in range(len(motifs))])
        score += min([rosalind2B.hamming_distance(motif, seq*len(motif)) for seq in 'ACGT'])
    return score


def greedyMotifSearch(Dna, k, t):
    """return a collection of strings BestMotifs"""
    BestScore = math.inf
    
    for i in range(len(Dna[0])-k+1):
        motifs = [Dna[0][i:i+k]]

        for j in range (1,t):
            profile = formProfile(motifs)
            consensus = rosalind2C.profile_most_probable(Dna[j],k,profile)
            
            motifs.append(consensus)
        
        score = getScore(motifs)

        if(score < BestScore):
            BestScore = score
            BestMotifs = motifs

    return BestMotifs

def read2D(filename):
    """Read 2D input data"""
    with open(filename, "r") as file:
        kt = file.readline().strip().split(" ")
        k = int(kt[0])
        t = int(kt[1])
        Dna = [line.strip() for line in file.readlines()]
        return k, t, Dna

if __name__ == "__main__":
    k, t, Dna = read2D("debug3.txt")
    res = greedyMotifSearch(Dna,k,t)

    for i in range(len(res)):
        print(res[i])
