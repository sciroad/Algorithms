import math
from collections import Counter, defaultdict
dist = defaultdict(lambda : Counter(""))
fact = dict()
powr = dict()
m = 10 ** 9 + 7
def initialize(s):
    fact[0], powr[0], dist[0] = 1, 1, Counter(s[0])
    for j in range(1, len(s)):
        fact[j] = (j * fact[j - 1]) % m
        dist[j] = dist[j-1] + Counter(s[j])

initialize("aabb")
print(dist)
factorials={}
l_dict=[]
def initialize(s):
    # This function is called once before all queries.  
    d={}
    factorials[0]=1
    factorials[1]=1
    d[s[0]]=1
    for i in range(1,len(s)):
        if s[i] not in d:
            d[s[i]]=0
        d[s[i]]+=1
        l_dict.append(d.copy())
        factorials[i+1]=(factorials[i]*(i+1))%1000000007

def answerQuery(l, r):
    def dif(d1,d2):
        d3={}
        for key in d2:
            if key not in d1:
                d3[key]=d2[key]
            else:
                d3[key]=d2[key]-d1[key]
        return d3
    count=l_dict[r-1]
    if l>1:
        count=dif(l_dict[l-2],l_dict[r-1])
    ones=0
    fac=1
    result=0
    for num in count.values():
        ones+=num%2
        numdiv2=num//2
        result+=numdiv2
        fac=(factorials[numdiv2]*fac)%1000000007
    result=factorials[result]//fac
    if ones>0:
        result*=ones
    return result%1000000007
s="wldsfubcsxrryqpqyqqxrlffumtuwymbybnpemdiwyqz"
print(answerQuery(13,34))