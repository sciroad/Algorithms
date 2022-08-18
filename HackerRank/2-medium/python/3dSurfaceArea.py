def surfaceArea(A):
    def heightDif(x, y):
        totalDif = 0
        if x == 0:
            totalDif += A[x][y]
        elif A[x][y]-A[x-1][y] > 0:
            totalDif += A[x][y]-A[x-1][y]
        if y == 0:
            totalDif += A[x][y]
        elif A[x][y]-A[x][y-1] > 0:
            totalDif += A[x][y]-A[x][y-1]
        if x == len(A)-1:
            totalDif += A[x][y]
        elif A[x][y]-A[x+1][y] > 0:
            totalDif += A[x][y]-A[x+1][y]
        if y == len(A[x])-1:
            totalDif += A[x][y]
        elif A[x][y]-A[x][y+1] > 0:
            totalDif += A[x][y]-A[x][y+1]
        return totalDif

    totalArea = 2*len(A)*len(A[0])

    for i in range(len(A)):
        for j in range(len(A[0])):
            totalArea += heightDif(i, j)
    return totalArea
