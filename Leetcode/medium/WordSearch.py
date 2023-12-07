class Solution:
    def exist(self, board, word) :
        
        def dfs(i,j,index):
            if index>=len(word):
                return True
            if i>=len(board) or i<0 or j<0 or j>=len(board[0]) or word[index]!=board[i][j]:
                return False
            s,board[i][j]=board[i][j],"-"
            res=dfs(i+1,j,index+1) or dfs(i-1,j,index+1) or dfs(i,j+1,index+1) or dfs(i,j-1,index+1)
            board[i][j]=s
            return res



        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and dfs(i,j,0):
                    return True
        return False

s=Solution()
print(s.exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
,"aaaaaaaaaaaaa"))