"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

# my approach. O(M + N) scan. start at the top right corner (botleft would also work). then see if target is smaller or larger.
# if smaller, we know we must move towards the left, and reduce the search space. if the target is bigger, we must go down, ignoring
# all the values above


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            val = matrix[row][col]
            if target == val:
                return True
            elif target < val:
                col -= 1
            else:
                row += 1
        return False
