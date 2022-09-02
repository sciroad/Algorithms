from bisect import bisect_left, insort_left

def activityNotifications(expenditure, d):
    
    listD = sorted(expenditure[:d])

    def median():
        return listD[d//2] if d%2 == 1 else ((listD[d//2] + listD[d//2-1])/2)
    result=0
    for i in range(d,len(expenditure)):
        if expenditure[i] >= 2*median(): result += 1
        del listD[bisect_left(listD, expenditure[i-d])]
        insort_left(listD, expenditure[i])
    return result