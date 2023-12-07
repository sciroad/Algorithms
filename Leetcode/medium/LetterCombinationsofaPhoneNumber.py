class Solution:
    def letterCombinations(self, digits):
        letters={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',   
        }
        res=[]
        cur=[]
        def bt(index):
            if index==len(digits):
                res.append(''.join(cur[:]))
                return
            for i in range(len(letters[digits[index]])):
                cur.append(letters[digits[index]][i])
                bt(index+1)
                cur.pop()
        bt(0)
        return res
s=Solution()
print(s.letterCombinations('23'))