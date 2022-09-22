def gridlandMetro(n, m, k, track):
    # Write your code here
    d={}
    total=n*m
    for i in range(k):
        r=track[i][0]
        c1=track[i][1]
        c2=track[i][2]
        if r not in d:
            d[r]= [c1,c2]
        elif c1>d[r][1]:
            total-=c2-c1+1
        elif c2>d[r][1]:
            d[r][1]=c2
    tracks=0
    for r in d:
        tracks+=d[r][1]-d[r][0]+1
    return total-tracks


arr = [[2, 1, 5], [2, 6, 7], [2, 6, 8]]
print(gridlandMetro(2, 9, 3, arr))
