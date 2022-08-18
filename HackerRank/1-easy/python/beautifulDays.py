from math import remainder


def beautifulDays(i, j, k):
    # Write your code here
    count=0
    for x in range(i, j + 1):
        reversed=int(str(x)[::-1])
        absulute=abs(x-reversed)
        rem=absulute%k
        if rem==0:
            count=count+1
    return count
        
  