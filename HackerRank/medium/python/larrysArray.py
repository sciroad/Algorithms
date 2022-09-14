def larrysArray(A):
    counter=0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                counter+=1
    if counter%2==0:
        return "YES"
    return "NO"