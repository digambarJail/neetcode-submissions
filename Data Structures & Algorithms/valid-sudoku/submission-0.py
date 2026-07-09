class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowdict = {}
        coldict = {}
        boxdict = {}

        for i in range(9):
            rowdict[i] = []
            coldict[i] = []

        for i in range(3):
            for j in range(3):
                boxdict[(i, j)] = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowdict[i] or board[i][j] in coldict[j]:
                    return False
                rowdict[i].append(board[i][j])
                coldict[j].append(board[i][j])
            
                temp_i = i // 3
                temp_j = j // 3

                if board[i][j] in boxdict[(temp_i, temp_j)]:
                    return False
                boxdict[(temp_i, temp_j)].append(board[i][j])

        return True
