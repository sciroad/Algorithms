class Solution:
    def subsetsWithDup(self, nums):
        cur=[]
        res=[]
        def bt(i,cur):
            if i ==len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            bt(i+1,cur)
            cur.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            bt(i+1,cur)
        bt(0,[])
        return res


sol=Solution()
nums=[1,2,2]    
print(sol.subsetsWithDup(nums))

