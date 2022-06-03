from typing import Dict, List
def EulerianCycle(graph: Dict[str, List[str]], node: str):
    """return an Eulerian cycle in graph"""
    EulerianPath = [node]
    while(graph[node]):
        EulerianPath = EulerianPath[:1] + EulerianCycle(graph,graph[node].pop()) + EulerianPath[1:]
    return EulerianPath

def read4(filename):
    with open(filename, "r") as file:
        graph = {}
        for line in file:
            from_node, to_nodes = line.strip().split(' -> ')
            graph[from_node] = to_nodes.split(",")
    return graph

if __name__ == "__main__":
    graph = read4("debug16.txt")
    # original = ["0 -> 3", "1 -> 0", "2 -> 1,6", "3 -> 2", "4 -> 2", "5 -> 4", "6 -> 5,8","7 -> 9","8 -> 7","9 -> 6"]
    # graph = {}
    # for str in original:
    #     from_node, to_nodes = str.strip().split(' -> ')
    #     graph[from_node] = to_nodes.split(",")
    EulerianPath = EulerianCycle(graph,list(graph.keys())[0])
    print('->'.join(EulerianPath))