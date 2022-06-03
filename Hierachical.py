
def Hier(matrix, n):
    clusters = [[i] for i in range(n)]
    graph = []

    while len(clusters) > 1:
        min = 1000000
        for i in range(len(clusters)-1):
            for j in range(i+1,len(clusters)):
                dist = 0
                for k in clusters[i]:
                    for l in clusters[j]:
                        dist += matrix[k][l]
                dist = dist / (len(clusters[i]) * len(clusters[j]))

                if dist < min:
                    min = dist
                    closesti = i
                    closestj = j
        
        new = clusters[closesti] + clusters[closestj]
        
        clusters = [cluster for cluster in clusters if cluster not in [clusters[closesti],clusters[closestj]]]
        clusters.append(new)
        graph.append(new)

    return graph

def read26(filename):
    with open(filename, "r") as file:
        n  = int(file.readline())
        matrix = []

        for line in file.readlines():
            temp = []
            for e in line.split(' '):
                temp.append(float(e))
            matrix.append(temp)

        return n,matrix

if __name__ == "__main__":
    n,matrix = read26("debug26.txt")
    graph = Hier(matrix, n)

    for g in graph:
        print(' '.join([str(i+1) for i in g]))
