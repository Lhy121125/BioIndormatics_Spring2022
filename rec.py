from Debruijn import debruijn
from Path import getInDegrees, getOutDegrees, init, EulerianPath
import sys
sys.setrecursionlimit(10000)

def reconstruction(kmers):
    graph = debruijn(kmers)
    #print(graph)
    inD = getInDegrees(graph)
    #print(inD)
    out = getOutDegrees(graph)
    #print(out)
    initialNode = init(graph,inD,out)
    #print(init)
    path = EulerianPath(graph,out,initialNode)
    res = path[0][:-1]
    for p in path:
        res += p[-1]
    return res
    

def read7(filename):
    with open(filename, "r") as file:
        k = int(file.readline())
        kmers = [line.strip() for line in file.readlines()]
        return kmers

if __name__ == "__main__":
    kmers = read7("debug18.txt")
    #kmers = ["CTTA","ACCA","TACC","GGCT","GCTT","TTAC"]
    #debruijnGraph = debruijn(kmers)
    #sorted(debruijnGraph)
    print(reconstruction(kmers))
