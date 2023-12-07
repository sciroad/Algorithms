class Solution:
    def dailyTemperatures(self, t):
        
        stack = [len(t)-1]
        result = [0] * len(t) 

        for i in range(len(t)-2,-1,-1):
            
            if t[i] < t[stack[-1]]:
                if stack:
                    result[i]=stack[-1]-i
                stack.append(i)
                
            else:

                while stack and t[i] >= t[stack[-1]]:
                    stack.pop()

                if stack:
                    result[i]=stack[-1]-i
                stack.append(i)
        
        return result

s= Solution()
t = [89,62,70,58,47,47,46,76,100,70]


print(s.dailyTemperatures(t))