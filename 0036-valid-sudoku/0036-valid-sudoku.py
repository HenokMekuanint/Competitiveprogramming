class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            ans=set()
            for j in range(len(board[i])):
                if board[i][j]!="." and board[i][j] in ans:
                    return False
                elif board[i][j]!=".":
                    ans.add(board[i][j])
        for j in range(len(board[0])):
            ans=set()
            for i in range(len(board)):
                if board[i][j]!="." and board[i][j] in ans:
                    return False
                elif board[i][j]!=".":
                    ans.add(board[i][j])
        for i in range(0,len(board),3):
            for j in range(0,len(board[i]),3):
                ans=set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if (board[k][l] in ans):
                            return False
                        elif board[k][l]!=".":
                            if int(board[k][l])<1 or int(board[k][l])>9:
                                return False
                            else:
                                ans.add(board[k][l])
        return True
                    
                
        