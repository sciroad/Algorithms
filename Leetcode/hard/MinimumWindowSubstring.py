class Solution:
    def minWindow(self, s, t):
        l=0
        r=0
        mem={}
        for c in t:
            if c not in mem:
                mem[c]=0
            mem[c]+=1
        resLen=float("inf")
        res=""
        have=0
        need=len(mem)
        while r<len(s):
            if s[r] in mem:
                mem[s[r]]-=1
                if mem[s[r]]==0:
                    have+=1
            while have==need:
                if s[l] in mem:
                    mem[s[l]]+=1
                    if mem[s[l]]>0:
                        have-=1
                        sLen=r-l+1
                        if sLen<resLen:
                            resLen=sLen
                            res=s[l:r+1]
                        l+=1
                        break
                l+=1
            r+=1
        return res
s=Solution()

print(s.minWindow("ADOBECODEBANC","ABC"))