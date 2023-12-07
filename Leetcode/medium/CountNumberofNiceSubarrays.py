class Solution:
    def numberOfSubarrays(self, nums, k):
        res=0
        odd=[-1]
        for i in range(len(nums)):
            if nums[i]%2==1:
                odd.append(i)
        odd.append(len(nums))
        for i in range(1,len(odd)-k):
            res+=(odd[i]-odd[i-1])*(odd[i+k]-odd[i+k-1])
        return res
        


s=Solution()
print(s.numberOfSubarrays([1,1,2,1,1],3))