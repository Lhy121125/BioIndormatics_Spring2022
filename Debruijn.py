def debruijn(kmers):
    debruijnGraph = {}
    for i in range(len(kmers)):
        try:
            debruijnGraph[kmers[i][:-1]].append(kmers[i][1:])
        except:
            debruijnGraph[kmers[i][:-1]] = [kmers[i][1:]]
    
    return debruijnGraph

def read3(filename):
    with open(filename, "r") as file:
        
        kmers = [line.strip() for line in file.readlines()]
        return kmers

if __name__ == "__main__":
    #kmers = read3("debug15.txt")
    kmers = ["GAGG","CAGG","GGGG","GGGA","CAGG","AGGG","GGAG"]
    debruijnGraph = debruijn(kmers)
    #sorted(debruijnGraph)
    for key,value in sorted(debruijnGraph.items()):
        print(key + ' -> ' + ','.join(sorted([i for i in value])))
   
