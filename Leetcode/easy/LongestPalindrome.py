class Solution:
    def longestPalindrome(self, s: str) -> int:
        wl={s[0]}
        l=0
        for i in range(1,len(s)):

            if s[i] in wl:
                wl.remove(s[i])
                l+=2
            else:
                wl.add(s[i])
                
            print(wl)
        if len(s)%2==1:
            l+=1
        return l

s=Solution()
ss="abccccdd"

print(s.longestPalindrome(ss))
