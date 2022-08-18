def nonDivisibleSubset(k, s):
    remCount = {i: 0 for i in range(k)}
    for i in s:
        remCount[i % k] += 1
    mid = (k+1)//2
    count = 0
    for i in range(mid):
        if i == 0:
            if(remCount[i] != 0):
                count += 1
        else:
            if remCount[i] > remCount[k-i]:
                count += remCount[i]
            else:
                count += remCount[k-i]

    if k % 2 == 0:
        if(remCount[mid] != 0):
            count += 1
    return count
