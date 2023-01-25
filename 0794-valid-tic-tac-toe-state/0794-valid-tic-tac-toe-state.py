class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        ["OXX","XOX","OXO"]
        xcounter=0
        ocounter=0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=="X":
                    xcounter+=1
                elif board[i][j]=="O":
                    ocounter+=1
        if xcounter-ocounter>1 or xcounter-ocounter<0:return False
        ford=(board[0][0]+board[1][1]+board[2][2])
        revd=(board[2][0]+board[1][1]+board[0][2])
        if ford=="XXX" or revd=="XXX":
              if xcounter-ocounter==1:
                return True
              else:
                return False
        elif ford=="OOO" or revd=="OOO":
                if xcounter-ocounter==0:
                    return True
                else:
                    return False
        counter=0
        for i in range(len(board)):
            _str=""
            for j in range(len(board)):
                _str+=board[i][j]
            if (_str=="XXX" and xcounter-ocounter==1) or (_str=="OOO"and  xcounter-ocounter==0):
                return True
            elif (_str=="XXX" and xcounter-ocounter!=1)  or (_str=="OOO" and xcounter-ocounter!=0) :
                return False
        for j in range(len(board[0])):
            _str=""
            for i in range(len(board)):
                _str+=board[i][j]
            if (_str=="XXX" and xcounter-ocounter==1) or (_str=="OOO" and xcounter-ocounter==0):
                
                return True
            elif (_str=="XXX" and xcounter-ocounter!=1)  or (_str=="OOO" and xcounter-ocounter!=0):
                return False

        if xcounter-ocounter==1 or xcounter-ocounter==0:return True
                
                    
                
                

                    
        