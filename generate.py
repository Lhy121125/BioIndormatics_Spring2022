def composition(k,str):
    res = []
    for i in range(len(str)-k+1):
        res.append(str[i:i+k])
    return res

def read1(filename):
    """Read input data"""
    with open(filename, "r") as file:
        k= int(file.readline())
        str = file.readline()
        return k,str

if __name__ == "__main__":
    k,str = read1("inputt.txt")
    #k = 5
    #str = "CAATCCAAC"
    res = composition(k,str)
    res.sort()
    for s in res:
        print(s)