#Determine if a 9 x 9 Sudoku board is valid.
class Solution(object):
    def isValidSudoku(self, board):

        # Check rows
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                for k in range(j + 1, 9):
                    if board[i][j] == board[i][k]:
                        return False

        # Check columns
        for j in range(9):
            for i in range(9):
                if board[i][j] == ".":
                    continue
                for k in range(i + 1, 9):
                    if board[i][j] == board[k][j]:
                        return False

        # Check each 3x3 box
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        if board[i][j] == ".":
                            continue

                        for x in range(i, row + 3):
                            start = j + 1 if x == i else col

                            for y in range(start, col + 3):
                                if board[i][j] == board[x][y]:
                                    return False

        return True