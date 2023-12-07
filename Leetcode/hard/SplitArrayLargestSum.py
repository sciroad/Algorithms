class Solution:
    def splitArray(self, nums, k):
        l=nums[0]
        r=0
        for num in nums:
            if num<l:
                l=num
            r+=num
        m=0
        def partition(ul,k):
            current=0
            for num in nums:
                current+=num
                print("current:",current)
                if current>ul:
                    current=num
                    if num>ul:
                        return False
                    k-=1
                    if k==0:
                        return False
            return k>0
        res=r
        while l<=r:
            m=(l+r)//2
            p=partition(m,k)
            if p:
                res=m
                r=m-1
            else:
                l=m+1
        return res

s=Solution()
print(s.splitArray([2,3,1,2,4,3],5))


    