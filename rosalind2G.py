import numpy as np
import rosalind2B
import rosalind2C
import rosalind2E
import rosalind2F
import random



def profileRandom(Text,k,profile):
    """return the profile-randomly generated k-mer in a string Text"""
    probs = []
    kmers = []
    
    for kmer in rosalind2B.unique_kmer_composition(Text,k):
        prob = rosalind2C.probability(kmer,profile)
        kmers.append(kmer)
        probs.append(prob)
    
    probs /= np.sum(probs)
    index = np.random.choice(range(len(probs)), p=probs)
    return kmers[index]


def gibbsSample(Dna,k,t,N):
    """return the best Profile-randomly selected motifs"""
    BestMotifs = rosalind2F.randomize(k,Dna)
    motifs = BestMotifs
    BestScore = 100000

    for j in range(N):
        i =  random.randrange(t)
        motifs.pop(i)
        profile = rosalind2E.formProfile(motifs)
        motifi = profileRandom(Dna[i],k,profile)
        motifs.insert(i,motifi)
        score = rosalind2E.getScore(motifs)
        if score < BestScore:
            BestMotifs = motifs
            BestScore = score
    return BestMotifs


def run(Dna,k,t,N):
    """run Gibb Sample 20 times"""
    bestMotifs = []
    bestScore = 100000
    for i in range(20):
        motifs = gibbsSample(Dna,k,t,N)
        score = rosalind2E.getScore(motifs)
        if(score < bestScore):
            bestScore = score
            bestMotifs = motifs
    return bestMotifs

def read2G(filename):
    """Read 2G input data"""
    with open(filename, "r") as file:
        ktN = file.readline().strip().split(" ")
        k = int(ktN[0])
        t = int(ktN[1])
        N = int(ktN[2])
        Dna = [line.strip() for line in file.readlines()]
        return k, t, N, Dna


if __name__ == "__main__":
    k, t, N, Dna = read2G("input_5.txt")
    #Dna = (["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT","TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"])
    
    res = run(Dna,k,t,N)

    for i in range(len(res)):
        print(res[i])
