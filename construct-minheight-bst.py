"""
Given a sorted array with distinct integers, construct a Binary Search Tree
with minimum height
"""

# my approach: using the sorted property, make the root of each subtree to be the value
# at the middle index. keep creating "middles" by changing the left and right values, similar
# to a binary search

# O(n) time | O(n) space (since we need to store the BST in memory)


def minHeightBst(arr):
    return minHeightHelper(0, len(arr)-1, arr)


def minHeightHelper(left, right, arr):
    if left > right:
        return None
    mid = left + (right - left) // 2
    bst = BST(arr[mid])
    bst.left = minHeightHelper(left, mid - 1, arr)
    bst.right = minHeightHelper(mid + 1, right, arr)
    return bst
