class Solution:
    def subsets(self, nums) :
        res=[]
        current=[]
        def bt( i ):
            if i>=len(nums):
                res.append(current[:])
                return
            current.append(nums[i])
            bt(i+1)
            current.pop()
            bt(i+1)
        bt(0)
        return res
    
s=Solution()
nums=[1,2,3,4]
print(s.subsets(nums))