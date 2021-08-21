class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            tmp = []
            for col in range(cols):
                if(board[row][col].isdigit()):
                    tmp.append(board[row][col])
            if len(tmp) != len(set(tmp)):
                return False
            for ele in tmp:
                if int(ele) not in range(1,10):
                    return False
        for col in range(cols):
            tmp = []
            for row in range(rows):
                if(board[row][col].isdigit()):
                    tmp.append(board[row][col])
            if len(tmp) != len(set(tmp)):
                return False
            for ele in tmp:
                if int(ele) not in range(1,10):
                    return False
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                d = {}
                for i in range(n, n + 3):
                    for j in range(m, m + 3):
                        if board[i][j] == '.':
                            pass
                        elif board[i][j] in d:
                            return False
                        else:
                            d[board[i][j]] = True
        return True
                    
        
                
                    
                