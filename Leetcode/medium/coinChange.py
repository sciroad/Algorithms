class Solution:
    def coinChange(self, coins, amount):
        mem={}
        def dfs(i,a):
            if a==0:
                return 0
            if (i,a) in mem:
               return mem[(i,a)]
            if a<0:
                return float("inf")
            if i>=len(coins):
                return float("inf")
            mem[(i,a)]=float("inf")
            l=dfs(i,a-coins[i])
            r=dfs(i+1,a)
            mem[(i,a)]=min(mem[(i,a)],1+l,r)
            return mem[(i,a)]
        res=dfs(0,amount)
        return -1 if res==float("inf") else res
    
s=Solution()
print(s.coinChange([1,2,5],11))