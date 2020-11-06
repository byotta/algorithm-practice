"""
Given a binary search tree and a node p, find p's inorder successor and return it
"""

# my approach: if p has a right child, then we know the in order successor for p will be the leftmost child in its right subtree
# otherwise, we will simply perform an iterative inorder traversal, each time storing a previous value. if we find that the previous
# value is equal to p's value, then whatever node we are on currently will be the in order successor.


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        stack = []
        curr = root
        prev = float('inf')
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev == p.val:
                return curr
            prev = curr.val
            curr = curr.right
