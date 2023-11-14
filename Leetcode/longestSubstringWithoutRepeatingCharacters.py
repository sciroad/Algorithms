class Solution(object):
    def lengthOfLongestSubstring(self, s):

        """
        :type s: str
        :rtype: int
        """
        mem={}
        l=0
        r=0
        longest=0
        while r<len(s):
            if s[r] not in mem:
                mem[s[r]]=1
            else:
                mem[s[r]]+=1
            
            if mem[s[r]]>1:
                length=r-l
                if length>longest:
                    longest=length
                while mem[s[r]]>1:
                    mem[s[l]]-=1
                    l+=1
            r+=1
        if r-l>longest:
            longest=r-l
        return longest

s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))