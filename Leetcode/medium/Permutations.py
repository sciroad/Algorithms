class Solution:
    def permute(self,nums):
        
        if len(nums)==1:
            return [nums[:]]
        res=[]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
    

s=Solution()
nums=[1,2,3,4,5,6,7,8,9]
print(s.permute(nums))