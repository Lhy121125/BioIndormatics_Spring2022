import itertools
import math

def unique_kmer_composition(sequence, k):
    """Return set of unique k-mers in sequence"""
    k_mers = []
    for i in range (0,len(sequence)-k+1):
        k_mers.append(sequence[i:i+k])
    return k_mers

def hamming_distance(pattern1, pattern2):
    """Compute the hamming distance for patterns of identical length"""
    d = 0
    for i in range(0,len(pattern1)):
        if pattern1[i] != pattern2[i]:
            d+=1
    return d

def min_distance_to_sequence(pattern, sequence):
    """Minimum distance between pattern of length k and all k-mers in sequence"""
    min = 100000
    k_mers = unique_kmer_composition(sequence,len(pattern))
    for i in range(0,len(k_mers)):
        if hamming_distance(pattern,k_mers[i]) < min:
            min = hamming_distance(pattern,k_mers[i])
    return min
    

def distance_to_all_sequences(pattern, sequences):
    """Sum of all distances between pattern and strings in sequences"""
    dSum = 0
    for i in range(0,len(sequences)):
        dSum += min_distance_to_sequence(pattern,sequences[i])
    return dSum

def medianString(Dna, k):
    """return a k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern"""
    distance = math.inf
    median = ''
    all_patterns = ["".join(kmer) for kmer in itertools.product("ACGT",repeat=k)]
    for i in range(1,len(all_patterns)):
        pattern = all_patterns[len(all_patterns)-i]
        if distance_to_all_sequences(pattern,Dna) <= distance:
            distance = distance_to_all_sequences(pattern,Dna)
            median = pattern
    return median



def read2B(filename):
    """Read rosalind.info 2B input data"""
    with open(filename, "r") as file:
        # Recall that the file object maintains an internal pointer so you can use
        # multiple readline calls to read individual lines.
        k = int(file.readline().strip())
        
        # Similarly readlines will read the remaining lines in the file.
        # Here I am using a list comprehension to create a list of strings with any leading
        # or trailing whitespace removed.
        kmers = [line.strip() for line in file.readlines()]
        return kmers, k


if __name__ == "__main__":
    f = read2B("debug.txt")
    print(medianString(f[0],f[1]))
