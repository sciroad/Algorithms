class Solution:
    def permute(self, nums):
        res=[]
        cur=[]
        def bt():
            if len(nums)==0:
                res.append(cur[:])
                return
            for i in range(len(nums)):
                n=nums.pop(0)
                cur.append(n)
                bt()
                cur.pop()
                nums.append(n)
        bt()
        return res
s=Solution()
print(s.permute([1,2,3]))