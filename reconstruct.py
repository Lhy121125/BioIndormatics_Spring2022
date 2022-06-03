def reconstruct(strs):
    res = strs[0]
    k = len(strs[0])
    for i in range(1,len(strs)):
        res+=(strs[i][k-1])
    
    return res

def read2(filename):
    with open(filename, "r") as file:
        
        kmers = [line.strip() for line in file.readlines()]
        return kmers

if __name__ == "__main__":
    kmers = read2("debug14.txt")
    print(reconstruct(kmers))