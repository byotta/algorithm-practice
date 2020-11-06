"""
traverse a binary tree in order, without using recursion
"""

# my approach: keep a stack, and result list and current pointer. while the current pointer is not null, or the stack has elements in it
# keep placing all left elements of the tree into the stack. once there are none in that "left line", place the current node in the
# result, and move onto the right elements


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
