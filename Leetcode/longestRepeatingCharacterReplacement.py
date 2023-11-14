class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mem={}
        l=0
        r=0
        maxLen=0
        count=0
        while r<len(s):
            if s[r] not in mem:
                mem[s[r]]=0
            mem[s[r]]+=1
            count =max(count, mem[s[r]])
            while r-l+1-count>k:
                mem[s[l]]-=1
                l+=1
            maxLen=max(maxLen,r-l+1)
            r+=1
        return maxLen


s=Solution()
print(s.characterReplacement("ABAB",2))
        




















































        # mem={}
        # maxCount=0
        # start=0
        # end=0
        # maxLen=0
        # while end<len(s):
        #     if s[end] not in mem:
        #         mem[s[end]]=0
        #     mem[s[end]]+=1
        #     maxCount=max(maxCount,mem[s[end]])
        #     while end-start+1-maxCount>k:
        #         mem[s[start]]-=1
        #         start+=1
        #     maxLen=max(maxLen,end-start+1)
        #     end+=1
        # return maxLen