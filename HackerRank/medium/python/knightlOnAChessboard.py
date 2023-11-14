from collections import deque


def knightlOnAChessboard(n):
    def check_pairs(i,j,a,b,n):
        pos = [(a,b),(a,-b),(-a,b),(-a,-b),(b,a),(b,-a),(-b,a),(-b,-a)]
        moves = {(i+x,j+y):1 for x,y in pos if 0<=i+x<n and 0<=j+y<n}
        return moves
    def bfs(a,b,n):
        q=deque([(0,0,0)])
        visited = {(0,0):1}
        while q:
            i, j, count = q.popleft()
            pos_pairs=check_pairs(i,j,a,b,n)
            for pair in pos_pairs:
                if pair==(n-1,n-1):
                    return count+1
                if pair not in visited:
                    visited[pair]=1
                    q.append((pair[0],pair[1],count+1))
        return -1
    result=[]
    for i in range(1,n):
        temp=[]
        for j in range(1,n):
            temp.append(bfs(i,j,n))
        result.append(temp)
    return result