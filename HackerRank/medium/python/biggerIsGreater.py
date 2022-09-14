def biggerIsGreater(w):
    # Complete this function
    w = list(w)
    for i in range(len(w)-1, 0, -1):
        if w[i] > w[i-1]:
            for j in range(len(w)-1,i,-1):
                if w[j] > w[i-1]:
                    w[i-1], w[j] = w[j], w[i-1]
                    w[i:] = w[i:][::-1]
                    return ''.join(w)
    return 'no answer'

ipt="1234"
print(ipt[len(ipt)-1:1:-1])
