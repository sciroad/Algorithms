class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row=len(matrix)
        col=len(matrix[0])

        l=0
        r=row*col-1
        while l<=r:
            m=(l+r)//2
            posr=m//col
            posc=m%col
            val=matrix[posr][posc]
            if val==target:
                return True
            elif val>target:
                r=m-1
            else:
                l=m+1
        return False

s=Solution()
# print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3))
# [[1,3]]
# 3
print(s.searchMatrix([[1,3]],3))