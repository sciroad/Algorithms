def formingMagicSquare(s):
    allSquares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    minCost = 45
    for square in allSquares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(square[i][j]-s[i][j])
        print(cost)
        if minCost > cost:
            minCost = cost
    return minCost


s = [[2, 2, 7, ],
     [8, 6, 4],
     [1, 2, 9]]
print(formingMagicSquare(s))
