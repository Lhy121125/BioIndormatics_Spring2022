import numpy as np
import rosalind2B

def probability(k_mer, profile):
    """return the probability of a k_mer from a profile"""
    probability = 1
    for i in range (0, len(k_mer)):
        if k_mer[i] == "A":
            probability *= profile[0][i]
        if k_mer[i] == "C":
            probability *= profile[1][i]
        if k_mer[i] == "G":
            probability *= profile[2][i]
        if k_mer[i] == "T":
            probability *= profile[3][i]
    return probability




def profile_most_probable(sequence,k,profile):
    """return a Profile-most probable k-mer in a string"""
    k_mers = rosalind2B.unique_kmer_composition(sequence,k)
    max = -1
    most = ""
    for k_mer in k_mers:
        for i in range(0,len(k_mer)):
            if probability(k_mer,profile) > max:
                max = probability(k_mer,profile)
                most = k_mer
    return most

def read2C(filename):
    """Read 2C input data"""
    with open(filename, "r") as file:
        sequence = file.readline().strip()
        k = int(file.readline().strip())
        profile = np.loadtxt(file)  # Default type is float
        return sequence, k, profile

if __name__ == "__main__":
    sequence, k, profile = read2C("debug2.txt")
    print(profile_most_probable(sequence, k, profile))

