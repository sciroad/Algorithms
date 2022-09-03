def lilysHomework(arr):
    # Write your code here
    srt=sorted(arr)
    srt_rev=srt.copy()
    srt_rev.reverse()
    arr_idx={arr[i]:i for i in range(len(arr))}
    arr_idx_rev=arr_idx.copy()
    arr_rev=arr.copy()
    count=0
    count_rev=0
    for i in range(len(arr)):
        if arr[i]!=srt[i]:
            idx=arr_idx[srt[i]] 
            arr[i],arr[idx]=arr[idx],arr[i]
            arr_idx[arr[i]],arr_idx[arr[idx]]=i,idx
            count+=1
        if arr_rev[i]!=srt_rev[i]:
            idx=arr_idx_rev[srt_rev[i]] 
            arr_rev[i],arr_rev[idx]=arr_rev[idx],arr_rev[i]
            arr_idx_rev[arr_rev[i]],arr_idx_rev[arr_rev[idx]]=i,idx
            count_rev+=1
    if count_rev>count: return count
    return count_rev