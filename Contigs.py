from Debruijn import debruijn
from Path import getInDegrees, getOutDegrees

def getContigs(graph,node,inDegrees,outDegrees):
    cont = []
    for n in graph[node]:
        path = [node,n]
        inD = inDegrees.get(n)
        out = outDegrees.get(n)

        while inD == 1 and out == 1:
            node = n
            n = graph[node][0]
            path.append(n)
            inD = inDegrees.get(n)
            out = outDegrees.get(n)

        cont.append(path)
    
    return cont

def convert(graph):
    res = []
    inD = getInDegrees(graph)
    out = getOutDegrees(graph)
    for node in out:
        if(node not in inD):
            i = 0
        else:
            i = inD[node] 
        o = out[node]
        if(o > 0 and not(i==1 and o==1)):
            res.extend(getContigs(graph,node,inD,out))
    return res

def read7(filename):
    with open(filename, "r") as file:
        kmers = [line.strip() for line in file.readlines()]
        return kmers
  

if __name__ == "__main__":
    kmers = read7("debug19.txt")
    #kmers = ["ATG", "ATG","TGT","TGG","CAT","GGA","GAT","AGA"]

    graph = debruijn(kmers)
    paths = convert(graph)
    #print(graph)
    contigs = []	

    for path in paths:
        res = path[0]
        for p in path[1:]:
            if(res[-(len(p)-1):] == p[:len(p)-1]):
                res += p[-1]
            contigs.append(res)
    

    print(' '.join(contigs))