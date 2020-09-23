"""
Invert a binary tree.
"""

# my approach: using a helper function, for each node, swap its left and right children


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invertHelper(root)
        return root

    def invertHelper(self, node: TreeNode):
        if node is None:
            return
        temp = node.left
        node.left = node.right
        node.right = temp
        self.invertHelper(node.left)
        self.invertHelper(node.right)
