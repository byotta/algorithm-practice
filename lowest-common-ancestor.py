"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

# my approach: for each node, check to see if it is either p or q. if so, return it to the parent caller. if it is neither
# check its left subtree for the result, as well as the right subtree. if it occurs in both subtrees, we know it is a common ancestor
# we can return this node. if it does not occur in both subtrees, try to return the one it occurs in (if it does. if not, just return the
# result from the right subtree which would be null)


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root is p or root is q:
            return root
        leftRes = self.lowestCommonAncestor(root.left, p, q)
        rightRes = self.lowestCommonAncestor(root.right, p, q)
        if not leftRes:
            return rightRes
        if not rightRes:
            return leftRes
        return root
