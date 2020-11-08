"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where "adjacent" cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
"""

# my approach: DFS + backtracking. use an N^2 matrix loop to get all the starting positions for the word path
# then if the first letter matches, we can begin a DFS. in the DFS, we will iterate through all 4 directions
# each time we pick a direction, we increment the wordIndex (the place in the word we are looking at)
# if we go through all four directions and we could not get to the end of the word, return false for that
# starting position, and move onto the next starting position


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        n, m = len(board), len(board[0])
        dirs = dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(n):
            for j in range(m):
                firstLetter = board[i][j]
                if firstLetter == word[0]:
                    if self.dfs(board, i, j, word, 0, dirs):
                        return True
        return False

    def dfs(self, board, i, j, word, wordIndex, dirs):
        if wordIndex >= len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[wordIndex] != board[i][j]:
            return False
        oldLetter = board[i][j]
        # use a set or use this method to avoid revisiting elements in the DFS
        board[i][j] = "#"
        for direction in dirs:
            newI = direction[0] + i
            newJ = direction[1] + j
            if self.dfs(board, newI, newJ, word, wordIndex + 1, dirs):
                return True
        board[i][j] = oldLetter
        return False
