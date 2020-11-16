"""
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

"""
# my approach: treat the whole 2D matrix as one single sorted array. we can access the ith element in
# this sorted array, getting the row from index // numColumns (to see which row its in) and column from
# index % numColumns (to see how far into the row it is)


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r-l) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                l = mid + 1
        return False
