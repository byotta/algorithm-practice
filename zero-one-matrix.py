"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""

# my approach: loop through the given matrix. if we find a 1, perform a standard BFS from that cell

from collections import deque


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for i in matrix[0]] for x in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    res[i][j] = self.bfs(matrix, i, j)
        return res

    def bfs(self, matrix, i, j):
        n, m = len(matrix), len(matrix[0])
        dq = deque()
        dq.append((i, j, 0))
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while dq:
            queueLen = len(dq)
            for _ in range(queueLen):
                currElement = dq.popleft()
                currI, currJ, distance = currElement[0], currElement[1], currElement[2]
                for direction in directions:
                    newElement = (
                        (currI + direction[0], currJ + direction[1], distance + 1))
                    if newElement[0] < 0 or newElement[0] >= len(matrix) or newElement[1] < 0 or newElement[1] >= len(matrix[0]):
                        continue
                    if matrix[newElement[0]][newElement[1]] == 0:
                        return newElement[2]
                    dq.append(newElement)
        return -1
