
def distance(A, B):
    dist = 0.0
    for i in range(len(A)):
        dist += (A[i] - B[i]) ** 2
    dist = dist ** 0.5
    return dist



def toClusters(centers,points,k):
    clusters = {x:[] for x in range(k)}
    # print(centers)
    # print("--------")

    for i in range(len(points)):
        closest = 100000
        center = 0
        for j in range(k):
            # print(type(centers[j]))
            # print(type(points[i]))
            dist = distance(centers[j],points[i])
            if dist < closest:
                closest = dist
                center = j
        clusters[center].append(i)
    return clusters


def getCenter(points,m):
    """clusters to center"""
    center = [0.0] * m
    for i in range(len(points)):
        for j in range(m):
            center[j] += float(points[i][j])/len(points)

    return center

def toCenters(points,clusters,m):
    """clusters to center"""
    centers = []

    for i in clusters:
        temp = []
        for j in clusters[i]:
            temp.append(points[j])
        center = getCenter(temp,m)
        centers.append(center)
    
    return centers


def lloyd(points,k,m):
    """Return a set Centers consisting of k points (centers) resulting 
    from applying the Lloyd algorithm to Data and Centers"""
    centers = points[0:k]

    while True:
        #clusters = defaultdict(list)

        clusters = toClusters(centers,points,k)
        new = toCenters(points,clusters,m)
            #clusters[tuple(center)].append(point)
        
        # for i in range(k):
        #     new[i] = toCenters(clusters[tuple(centers[i])],m)
    
        if new == centers:
            break

        centers = new
    
    return centers

def read23(filename):
    with open(filename, "r") as file:
        km = file.readline().split()
        k = int(km[0])
        m = int(km[1])
        points = [[float(i) for i in line.split()] for line in file.readlines()]
        #print(points)
        return k,m,points

if __name__ == "__main__":
    k,m,points = read23("debug23.txt")
    centers = lloyd(points,k,m)

    for center in centers:
        print(" ".join(map(str,center)))