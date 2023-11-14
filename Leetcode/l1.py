class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 1
        r = 0
        total = 0
        while(l < len(height)):
            if height[l-1] > height[l]:
                r = self.goForward(height, height[l-1], l)
                print(l-1,r)
                if(r == -1):
                    l+=1
                    continue
                h = min(height[l-1], height[r])
                while(l < r):
                    sumOf = h-height[l]
                    if sumOf > 0:
                        total += sumOf
                    l += 1
            l += 1

        return total

    def goForward(self, height, limit, r):
        init_r, max_r = r, r
        while(r < len(height) and height[r] < limit):
            
            if height[max_r] <= height[r]:
                max_r = r
            print("max_r", max_r, "height[max_r]", height[max_r])
            r += 1
        print(r, max_r, init_r)
        if r == len(height):
            if max_r != init_r:
                return max_r
            else: 
                return -1
        return r


s = Solution()
# print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap([5,4,1,2]))
