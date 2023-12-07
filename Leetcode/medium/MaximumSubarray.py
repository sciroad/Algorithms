class Solution:
    def maxSubArray(self, nums):
        r=0
        current=0
        maxSum=nums[0]
        while r<len(nums):
            current+=nums[r]
            if current>maxSum:
                maxSum=current
            current=max(0,current)
            r+=1
        return maxSum

s=Solution()
print([-2,1,-3,4,-1,2,1,-5,4])
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
            
