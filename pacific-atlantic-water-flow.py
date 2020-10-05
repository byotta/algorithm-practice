"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
"""

# my approach: keep two sets: one with the indices that the pacific water can reach, and one with the indices that the atlantic water can reach
# in the end, we will return the intersection of these two sets. we will use dfs to build up the sets.
  def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
       if len(matrix) < 1:
            return []
        pacific, atlantic = set(), set()
        n, m = len(matrix), len(matrix[0])
        directions = [(-1, 0), (0, 1), (1,0), (0,-1)]

        def dfs(i, j, specificSet):
            if (i, j) in specificSet:
                return
            specificSet.add((i, j))
            for direction in directions:
                newI = i + direction[0]
                newJ = j + direction[1]
                if 0 <= newI < n and 0 <= newJ < m and matrix[newI][newJ] >= matrix[i][j]:
                    dfs(newI, newJ, specificSet)

        for j in range(m):
            dfs(0, j, pacific)
            dfs(n-1, j, atlantic)
        for i in range(n):
            dfs(i, 0, pacific)
            dfs(i, m-1, atlantic)
        res = []
        for elem in pacific & atlantic:
            res.append(list(elem))
        return res
