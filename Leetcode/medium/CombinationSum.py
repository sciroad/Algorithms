class Solution:
    def combinationSum(self, candidates, target):
        res=[]
        com=[]
        resSet=set()
        def dfs(i,target):
            if target==0 and set(com) not in resSet:
                res.append(com[:])
                return
            elif target<0 or i>=len(candidates):
                return
            com.append(candidates[i])
            dfs(i,target-candidates[i])
            com.pop()
            dfs(i+1,target)
            
        dfs(0,target)    
        return res


s=Solution()
candidates = [2,3,6,7]
target = 7
print(s.combinationSum(candidates,target))