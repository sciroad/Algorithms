def highestValuePalindrome(s, n, k):
    # Write your code here
    s=list(s)
    mark=[False]*n
    l=0
    r=len(s)-1
    while l<=r:
        if s[l]!=s[r]:
            if s[l]>s[r]:
                s[r]=s[l]
                mark[r]=True
            else:
                s[l]=s[r]
                mark[l]=True
            k-=1
        if k<0:
            return "-1"
        l+=1
        r-=1
    if k > 0:
        l=0
        r=len(s)-1
        while l<=r:
            if l==r and k==1:
                s[l]='9'
                k-=1
            elif s[l]<'9':
                if (mark[l] or mark[r])and k>=1:
                    s[l]=s[r]='9'
                    k-=1
                elif k>=2:
                    s[l]=s[r]='9'
                    k-=2
            if k==0:
                break
            l+=1
            r-=1
    return "".join(s)
