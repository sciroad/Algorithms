class Solution:
    def largestRectangleArea(self, heights):
        stack=[]
        aMax=0
        for i in range(len(heights)):
            idx=i
            while stack and stack[-1][0]>heights[i]:
                h,idx=stack.pop()
                a=h*(i-idx)
                if aMax<a:
                    aMax=a
            stack.append((heights[i],idx))
            

        while stack:
            h,idx=stack.pop()
            a=h*(len(heights)-idx)
            if aMax<a:
                aMax=a
        return aMax


s=Solution()
heights=[4,2,0,3,2,5]

print(s.largestRectangleArea(heights))