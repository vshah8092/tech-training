class Solution:
    
    def checkList(self, l):
        for j in range(1, 10):
            if l.count(str(j)) > 1:
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            if not self.checkList(i):
                return False
        for i in range(0, 9):
            if not self.checkList([board[0][i], board[1][i], board[2][i], board[3][i],\
                            board[4][i], board[5][i], board[6][i], board[7][i], board[8][i]]):
                return False
        d = {}
        for i in range(9):
            for j in range(9):
                if str(i // 3) + str(j // 3) in d:
                    d[str(i // 3) + str(j // 3)].append(board[i][j])
                else:
                    d[str(i // 3) + str(j // 3)] = [board[i][j]]
        for i in d:
            if not self.checkList(d[i]):
                return False
        return True