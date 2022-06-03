from Viterbi import read8

def probability(x, Alphabet, States, Transition, Emission):
    """Return the probability Pr(x) that the HMM emits x."""
    front = [[0] * len(x) for _ in range(len(States))]
    for i in range(len(States)):
        front[i][0] = 1.0 / len(States) * Emission[i][Alphabet[x[0]]]
    for i in range(len(x) - 1):
        for j in range(len(States)):
            front[j][i+1] = Emission[j][Alphabet[x[i+1]]] * sum(front[k][i] * Transition[k][j] for k in range(len(States)))

    return sum(front[k][-1] for k in range(len(States)))

if __name__ == "__main__":
    x,Alphabet,States,Transition,Emission = read8("debug21.txt")

    print(probability(x,Alphabet,States,Transition,Emission))