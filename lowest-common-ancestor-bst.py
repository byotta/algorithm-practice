"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes 
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

"""

# my approach: once we have found a node such that its value falls between p and q's values,
# we can return that node. however, until then we can keep dropping half the tree, using the BST
# property to reduce the search space


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
