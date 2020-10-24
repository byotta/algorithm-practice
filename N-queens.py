"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
"""

# Classic N-Queens problem

# my approach: recursive backtracking. take a column, and try to place a queen in each row that doesnt conflict with previous placements
# if we cant place a queen, go back, undo and try the next cell


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for i in range(n)] for j in range(n)]
        res = []
        self.helper(board, 0, res)
        return res

    def helper(self, board, currCol, res):
        if currCol >= len(board):
            res.append(self.generateSolution(board))
            return
        for row in range(len(board)):
            if self.isValid(board, row, currCol):
                board[row][currCol] = 'Q'
                self.helper(board, currCol + 1, res)
                board[row][currCol] = '.'

    def isValid(self, board, row, col):
        n = len(board)
        for i in range(col+1):  # go across
            if board[row][i] == 'Q':
                return False
        for i in range(row+1):  # go down
            if board[i][col] == 'Q':
                return False

        topLeft_i, topLeft_j = row, col
        while topLeft_i >= 0 and topLeft_j >= 0:
            if board[topLeft_i][topLeft_j] == 'Q':
                return False
            topLeft_i -= 1
            topLeft_j -= 1

        botLeft_i, botLeft_j = row, col
        while botLeft_i < len(board) and botLeft_j >= 0:
            if board[botLeft_i][botLeft_j] == 'Q':
                return False
            botLeft_i += 1
            botLeft_j -= 1
        return True

    def generateSolution(self, board):
        n = len(board)
        res = []
        for i in range(n):
            row = ""
            for j in range(n):
                if board[i][j] == '.':
                    row += '.'
                elif board[i][j] == 'Q':
                    row += 'Q'
            res.append(row)
        return res
