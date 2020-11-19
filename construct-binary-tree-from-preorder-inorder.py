"""
Given preorder and inorder traversal of a tree, construct the binary tree.
"""

# approach. we can get the root quickly from the preorder traversal for each subtree. and we know what is on the left subtree
# and the right subtree of each subtrees root, by indexing into the given inorder array


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.compute(0, 0, len(inorder)-1, preorder, inorder)

    def compute(self, preStart, inStart, inEnd, preorder, inorder):
        if preStart >= len(preorder) or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart])

        inorderRootIndex = inorder.index(root.val)

        root.left = self.compute(
            preStart + 1, inStart, inorderRootIndex - 1, preorder, inorder)
        root.right = self.compute(preStart + inorderRootIndex -
                                  inStart + 1, inorderRootIndex + 1, inEnd, preorder, inorder)

        return root
