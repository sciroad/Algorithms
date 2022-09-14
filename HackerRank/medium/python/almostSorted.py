def almostSorted(arr):
    l = len(arr)
    F = False
    E = False
    for f in range(0, l-1):
        if arr[f] > arr[f+1]:
            F = True
            break
    if not F:
        print("yes")
        return
    for e in range(l-1, f,-1):
        if arr[e] < arr[e-1]:
            if e != l-1 and arr[f] > arr[e+1]:
                print("no")
                return
            if f != 0 and arr[e] < arr[f-1]:
                print("no")
                return
            E = True
            break
    if E and F:
        if f+2 < e and arr[f+1] > arr[f+2]:
            arr[f:e+1] = arr[f:e+1][::-1]
            for i in range(f, e):
                if arr[i] > arr[i+1]:
                    print("no")
                    return
            print("yes")
            print("reverse", f+1, e+1)
            return
        print("swap", f+1, e+1)
        return
    print("no")


arr = [1, 5, 4, 3, 2, 6]
arr2=[3, 1, 2]
arr3=[4, 2] 
almostSorted(arr3)
