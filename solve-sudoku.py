"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
"""

# my approach:
# recursive backtracking. iterate through the entire board each recursive call. if the current cell is a '.' then we know we
# should try to place a number there. iterate through all numbers 1 - 9. if that number can be placed there (doesnt clash with
# row, col, or 3x3 grid there) then we can keep it and move onto the next call. in the next calls, if we cant place any numbers
# in a cell, we will return False and come back to the original call, then remove that number we chose. eventually, we will find
# a permutation where we iterate through the entire board, and dont return false (see the last return True, after both loops)
# then we know the board is solved, and since we passed the board by reference, we can stop there


class Solution(object):
    def solveSudoku(self, board):
        """
        : type board: List[List[str]]
        : rtype: None Do not return anything, modify board in -place instead.
        """
        self.helper(board)

    def helper(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in range(1, 10):  # try placing 1 thru 9
                        if self.isValid(board, i, j, str(num)):
                            board[i][j] = str(num)
                            if self.helper(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, row, col, num):
        # check row (left thru right)
        for i in range(9):
            if board[row][i] == num:
                return False

        # check col (top thru bot)
        for i in range(9):
            if board[i][col] == num:
                return False

        # check 3x3 square:
        rowStart = row // 3 * 3
        colStart = col // 3 * 3
        # [rowStart][colStart] will be the topleft cell of the 3x3 grid
        rowEnd = rowStart + 3
        colEnd = colStart + 3
        i, j = rowStart, colStart
        while i < rowEnd:
            while j < colEnd:
                if board[i][j] == num:
                    return False
                j += 1
            j = colStart
            i += 1
        return True
