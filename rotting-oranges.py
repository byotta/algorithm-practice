"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
"""

# my approach: simple BFS using a queue, starting from multiple sources. 
# keep a counter for the number of minutes passed
from collections import deque
class Solution(object):
    def orangesRotting(self,grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        dq = deque()
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        freshCount = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dq.append((i,j))
                elif grid[i][j] == 1:
                    freshCount += 1
        if freshCount == 0:
            return 0
        
        minutes = 0
        while dq:
            queueLen = len(dq)
            for _ in range(queueLen):
                currOrange = dq.popleft()
                for direction in directions:
                    newOrange = (currOrange[0] + direction[0], currOrange[1] + direction[1])
                    if newOrange[0] < 0 or newOrange[0] >= n or newOrange[1] < 0 or newOrange[1] >= m or grid[newOrange[0]][newOrange[1]] == 0 or grid[newOrange[0]][newOrange[1]] == 2:
                        continue
                    
                    grid[newOrange[0]][newOrange[1]] = 2
                    freshCount -= 1
                    dq.append(newOrange)
            minutes += 1
        return minutes - 1 if freshCount == 0 else -1