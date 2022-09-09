from collections import Counter
import math
def sherlockAndAnagrams(s):
    d={}
    # Write your code here
    def count(l):
        r= 0 
        i=0
        j=i+1
        l_l=len(l)
        while i<(l_l-1):
            c=1
            j=i+1
            while j<l_l:
                if l[i]==l[j]:
                    del l[j]
                    j-=1
                    l_l-=1
                    c+=1
                j+=1
            i+=1
            r+=math.comb(c,2)
        return r
    for i in range (len(s)):
        for j in range(i+1, len(s)+1):
            if j-i not in d:
                d[j-i]=[]
            d[j-i].append(Counter(s[i:j]))
    result= 0
    print(d)
    for key in d:
        result+=count(d[key])
    return result
print(sherlockAndAnagrams("kkkk"))