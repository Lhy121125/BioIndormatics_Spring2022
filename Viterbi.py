def decode(x,alphabet,States,Transition,Emission):
    """Given a string x, followed by the alphabet Σ from which x was constructed, 
    followed by the states States, transition matrix Transition, and emission 
    matrix Emission of an HMM (Σ, States, Transition, Emission);
    return a path that maximizes the (unconditional) probability Pr(x, π) over 
    all possible paths π."""

    front = []
    back = []
    numStates = len(States)
    for i in range(numStates):
            front.append([0]*len(x))
            back.append([0]*len(x))
    
    for i in range(numStates):
        front[i][0] = 1.0/numStates * Emission[i][alphabet[x[0]]]

    for i in range(len(x)-1):
        for j in range(numStates):
            front[j][i+1] = Emission[j][alphabet[x[i+1]]] * max(front[k][i] * Transition[k][j] for k in range(len(States)))
            back[j][i+1] = max(range(len(States)),key=lambda l: front[l][i] * Transition[l][j])
    
    res = []
    index = max(range(len(States)), key=lambda l: front[l][-1])
    for i in range(len(front[0]) - 1, -1, -1):
        res.append(States[index])
        index = back[index][i]

    return (''.join(res[::-1]))

def read8(filename):
    with open(filename, "r") as file:
        x = file.readline().split()[0]
        file.readline()
        Alph = file.readline()
        Alpha = dict((k,v) for k,v in enumerate(Alph.split()))
        Alphabet = {v: k for k, v in Alpha.items()}
        file.readline()
        Sta = file.readline()
        States = Sta.split()
        file.readline()
        Trans = file.readline().split()
        Transition = [list(map(float, file.readline().split()[1:])) for _ in range(len(Trans))]
        file.readline()
        file.readline()
        Emission = [list(map(float, line.split()[1:])) for line in file.readlines()]
        
        return x,Alphabet,States,Transition,Emission






if __name__ == "__main__":
    # Emission = [[0.117,0.691,0.192],[0.097,0.42,0.483]]
    # Transition = [[0.641,0.359],[0.729,0.271]]
    # Alphabet = {'x':0,'y':1,'z':2}
    # res = decode("xyxzzxyxyy",Alphabet,['A','B'],Transition,Emission)
    x,Alphabet,States,Transition,Emission = read8("debug20.txt")
    # print(x)
    # print(Alphabet)
    # print(States)
    # print(Transition)
    # print(Emission)

    print(decode(x,Alphabet,States,Transition,Emission))
