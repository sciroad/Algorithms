def extraLongFactorials(n):
    result=1
    for i in range(n,0,-1):
        result*=i
    print(result)

print(extraLongFactorials(5))