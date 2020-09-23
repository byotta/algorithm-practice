"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.
"""

# my approach: use a simple dfs, where in each recursive call we append to the current string if it is not a leaf,
# else we take the current string and append it to a passed in master-list. at the end, return the sum of this master list.


class Solution(object):
    # def sumNumbers(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    def sumNumbers(self, root):
        if root is None:
            return 0
        digits = []
        self.compute(root, str(root.val), digits)
        return sum([int(digit) for digit in digits])

    def compute(self, node, currentPathAsString, digits):
        if node is None:
            return
        if node.left is None and node.right is None:
            digits.append(currentPathAsString)
        if node.left:
            self.compute(node.left, currentPathAsString +
                         str(node.left.val), digits)
        if node.right:
            self.compute(node.right, currentPathAsString +
                         str(node.right.val), digits)
