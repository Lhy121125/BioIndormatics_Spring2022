from typing import Dict, List
from collections import Counter
from Eulerian import EulerianCycle

def getInDegrees(graph):
    inDegrees = {}
    for edges in graph.values():
        for edge in edges:
            if edge not in inDegrees:
                inDegrees[edge] = 0
            inDegrees[edge] += 1
    return inDegrees

def getOutDegrees(graph):
    outDegrees = {}
    for edges in graph.keys():
        outDegrees[edges] = len(graph[edges])
    return outDegrees

def init(graph, inDegrees, outDegrees):
    start = None

    for edge in graph.keys():
        out = outDegrees.get(edge) if outDegrees.get(edge) is not None else 0
        inD = inDegrees.get(edge) if inDegrees.get(edge) is not None else 0
        if(out - inD == 1):
            return edge
        
        if(outDegrees.get(edge)>0):
            start = edge
    return start


def EulerianPath(graph, outDegree, init):
    """return an Eulerian path in graph"""
    path = [init]
    #print(graph)
    while init in graph and len(graph[init])>0:
        #node = EulerianPath(graph, outDegree, graph[init].pop())
        path = path[:1] + EulerianPath(graph, outDegree, graph[init].pop()) + path[1:]
    return path

def read6(filename):
    with open(filename, "r") as file:
        graph = {}
        for line in file:
            from_node, to_nodes = line.strip().split(' -> ')
            graph[from_node] = to_nodes.split(",")
    return graph

if __name__ == "__main__":
    graph = read6("debug_17.txt")
    # original = ["0 -> 2", "1 -> 3", "2 -> 1", "3 -> 0,4", "6 -> 3,7","7 -> 8","8 -> 9","9 -> 6"]
    # graph = {}
    # for str in original:
    #     from_node, to_nodes = str.strip().split(' -> ')
    #     graph[from_node] = to_nodes.split(",")
    inD = getInDegrees(graph)
    out = getOutDegrees(graph)
    m = init(graph,inD,out)
    # print(m)
    path = EulerianPath(graph,out,m)
    print('->'.join(path))
