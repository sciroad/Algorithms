
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        closed={"}":"{",")":"(","]":"["}
        for c in s:
            if c not in closed:
                print("open")
                l.append(c)
            elif len(l)>0 and c in closed:
                print("closed")
                ph=l.pop()
                if ph!=closed[c]:
                    print("not equal")
                    return False
            else:
                print("empty")
                return False
        return True

s=Solution()
print(s.isValid("()"))