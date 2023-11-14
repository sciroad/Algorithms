def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    i = 1
    j = 0
    l = 1
    if len(s) <= 1:
        return len(s)
    mem = {s[0]: 1}
    while(i < len(s)):
        # print(i, j, mem, sep=", ")
        if s[i] not in mem:
            mem[s[i]] = 1
            i += 1
        elif mem[s[i]] < 1:
            mem[s[i]] += 1
            i += 1
        elif mem[s[i]] == 1:
            mem[s[i]] += 1
            if i-j>l:
                l = i-j
            while(mem[s[i]]>1 ):
                # print(i, j, mem, sep=", ")
                mem[s[j]] -= 1
                j += 1

            i+=1
    if i-j > l:
        return i-j
    return l

print(lengthOfLongestSubstring(s="abcabcbb"))