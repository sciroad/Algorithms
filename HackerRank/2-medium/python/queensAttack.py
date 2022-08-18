import math
def queensAttack(n, k, r_q, c_q, obstacles):
    moves_vertical = [-1, 0, 1]
    moves_horizontal = [-1, 0, 1]
    moves = [[x, y]
             for x in moves_vertical for y in moves_horizontal if x != 0 or y != 0]
    count = 0
    print(moves)
    for move in moves:
        max_r = calc(r_q, move[0])
        max_c = calc(c_q, move[1])
        max = max_r
        if max_r > max_c:
            max = max_c

        for obs in obstacles:
            r = obs[0]-r_q
            c = obs[1]-c_q
            if angle([r,c],move) ==0 :
                if move[0]!=0:
                    max=r//move[0]
                else:
                    max=c//move[1]
                break
        count += max
    return count

def calc(location, direction):
    if direction == -1:
        return location
    elif direction == 1:
        return n-location
    else:
        return 0

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

obstacles = [[5, 5], [4, 2], [2, 3]]
n = 5
k = 3
r_q = 4
c_q = 3

print(queensAttack(n, k, r_q, c_q, obstacles))
