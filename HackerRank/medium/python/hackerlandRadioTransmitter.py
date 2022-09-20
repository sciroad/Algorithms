def hackerlandRadioTransmitters(x, k):
    # Write your code here
    def jump(x, k, i):
        for j in range(i+1, len(x)):
            if x[j] - x[i] >= k:
                if x[j] - x[i] == k:
                    i = j
                    break
                i = j-1
                break
            if j == len(x)-1:
                return len(x)
        for j in range(i+1, len(x)):
            if x[j] - x[i] >= k:
                if x[j] - x[i] == k:
                    i = j
                    break
                i = j-1
                break
            if j == len(x)-1:
                return len(x)
        return i+1

    s = set(x)
    x = list(s)
    x.sort()
    i = 0
    result = 0
    print(x)
    while i < len(x):
        i = jump(x, k, i)
        result = result+1
    return result


x = [2, 2, 2, 2, 1, 1, 1, 1]
print(hackerlandRadioTransmitters(x, 2))