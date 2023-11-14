class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack=[]
        l = 1
        total = 0
        p=-1
        while(l < len(height)):
            if height[l-1] > height[l]:
                if p!=-1:
                    stack.append(p)
                    p=-1
                stack.append(l-1)
            elif height[l-1]!=height[l]:
                if p==-1 and len(stack)!=0:
                    p=stack.pop()
                if p!=-1:
                    total+=(min(height[p],height[l])-height[l-1])*(l-p-1)
                    if height[p]==height[l]:
                        p=-1
                    elif height[p]<height[l]:
                        height[l-1]=height[p]
                        p=-1
                        continue
            l += 1

        return total


s=Solution()
print(s.trap([4,2,0,3,2,5]))