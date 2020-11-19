"""
Given inorder and postorder traversal of a tree, construct the binary tree.
"""


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(len(postorder)-1, 0, len(inorder) - 1, inorder, postorder)

    def helper(self, postIndex, inStart, inEnd, inorder, postorder):
        if postIndex < 0 or inStart > inEnd:
            return None

        root = TreeNode(postorder[postIndex])

        # find where this root occurs in the inorder array
        inorderRootIndex = inorder.index(root.val)

        rightSubtreeWidth = inEnd - inorderRootIndex

        root.left = self.helper(postIndex - rightSubtreeWidth - 1,
                                inStart, inorderRootIndex - 1, inorder, postorder)
        root.right = self.helper(
            postIndex - 1, inorderRootIndex + 1, inEnd, inorder, postorder)

        return root
