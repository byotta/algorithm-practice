"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""

# key idea: pass in two references to a helper function. these references will follow a symmetric
# path


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.compute(root, root)

    def compute(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return self.compute(a.left, b.right) and self.compute(a.right, b.left)
