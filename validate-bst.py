"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# my approach: for each node, see if its values fall within a specific bound. for the root, this bound
# will be just default values of -inf +inf. but for its children, the left childrens bounds have a maximum
# of its parent, and the right child will have a minimum of its parent. if these conditions are not met
# we return False


def isValidBST(self, node):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def compute(node, lower=float('-inf'), upper=float('inf')):
        if node is None:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        if not compute(node.right, node.val, upper) or not compute(node.left, lower, node.val):
            return False
        return True
    return compute(node)
