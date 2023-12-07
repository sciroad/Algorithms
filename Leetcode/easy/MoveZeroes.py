class Solution:
    def moveZeroes(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=0
        while r<len(nums):
            if nums[l]!=0:
                l+=1
            else:
                if nums[r]!=0:
                    nums[l],nums[r]=nums[r],nums[l]
                    l+=1
            r+=1

s=Solution()
nums=[0,1,0,3,12]
nums=[0,0,1]
s.moveZeroes(nums)
print(nums)