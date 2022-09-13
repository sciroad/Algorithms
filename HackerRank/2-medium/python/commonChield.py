def commonChild(s1, s2):
    # Write your code here
    maxAt={}
    for i in range(0,len(s1)):
        iMax=0
        for j in range(len(s2)):
            jMax=maxAt.get(j,0)
            if jMax>iMax:
                iMax=jMax
            if s1[i]==s2[j]:
                maxAt[j]=iMax+1     
    return max(maxAt.values(),0)