class Solution:
    def findMin(self, nums):
        l=0
        r=len(nums)-1
        mi=nums[0]
        while l<=r:
            
            m=(l+r)//2
            print(nums[l:r+1],nums[m], "min:",mi)
            if nums[m]>nums[l]:
                mi=min(mi,nums[l])
                l=m+1
            else:
                mi=min(mi,nums[r])
                r=m-1
        return mi

s=Solution()
print(s.findMin([3,4,5,1,2]))