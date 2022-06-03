import numpy as np
import rosalind2C
import rosalind2B
import rosalind2E
import random

def randomize(k,Dna):
    """return randomly selected k-mers Motifs"""
    motifs = []
    for motif in Dna:
        n = random.randrange(len(Dna[0])-k)
        motifs.append(motif[n:n+k])
    return motifs

def MOTIFS(profile,Dna,k):
    """return the profile-most-probable 4-mer from each row of Dna"""
    motifs = []
    for motif in Dna:
        motifs.append(rosalind2C.profile_most_probable(motif,k,profile))
    return motifs


def randomizedMotifSearch(Dna,k,t):
    """return a collection BestMotifs resulting"""
    BestMotifs = randomize(k,Dna)
    BestScore = 1000000

    while True:
        profile = rosalind2E.formProfile(BestMotifs)
        motifs = MOTIFS(profile,Dna,k)
        
        score = rosalind2E.getScore(motifs)
        if(score < BestScore):
            BestMotifs = motifs
            BestScore = score
        else:
            return BestMotifs

def read2F(filename):
    """Read 2F input data"""
    with open(filename, "r") as file:
        kt = file.readline().strip().split(" ")
        k = int(kt[0])
        t = int(kt[1])
        Dna = [line.strip() for line in file.readlines()]
        return k, t, Dna

def run(Dna,k,t):
    """Run RandomizedMotifSearch 1000 times"""
    BestMotifs = []
    BestScore = 1000000
    for i in range (1000):
        motifs = randomizedMotifSearch(Dna,k,t)
        score = rosalind2E.getScore(motifs)
        if(score < BestScore):
            BestScore = score
            BestMotifs = motifs
    return BestMotifs


if __name__ == "__main__":
    k, t, Dna = read2F("input_4.txt")
    #Dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

    
    res = run(Dna,k,t)

    for i in range(len(res)):
        print(res[i])
