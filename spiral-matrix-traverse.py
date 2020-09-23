"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""

# my approach: the key point of this problem is knowing when to change directions, and which direction to go.
# if you keep a directions array, that makes the process much easier. given a specific direction, follow that direction
# until either you go out of bounds of the array, or you arrive at a cell you've seen, in which case, simply backtrack and
# change directions.


def spiralTraverse(array):
    # Write your code here.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    directionIndex = 0
    n, m = len(array), len(array[0])
    numElementsSeen = 0
    i, j = 0, 0
     res = []
      seenIndices = set()
       while numElementsSeen < n * m:
            currDirection = directions[directionIndex]
            element = array[i][j]
            seenIndices.add((i, j))
            res.append(element)
            i += currDirection[0]
            j += currDirection[1]
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in seenIndices:
                i -= currDirection[0]
                j -= currDirection[1]
                directionIndex += 1
                if directionIndex == 4:
                    directionIndex = 0
                currDirection = directions[directionIndex]
                i += currDirection[0]
                j += currDirection[1]
            numElementsSeen += 1
        return res
