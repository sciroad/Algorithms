def cardinalitySort(nums):
    # Write your code here
    mem={}
    for i in nums:
        car = bin(i).count("1")
        if car not in mem:
            mem[car]=[i]
        else:
            mem[car].append(i)
    res=[]
    mem=dict(sorted(mem.items()))
    print(mem)
    for key in mem:
        
        s=sorted(mem[key])
        res.extend(s)
    return res

cardinalitySort([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])