"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""

# my approach: perform a simple BFS. store the elements of each level in a list, and append that list to a master list
# only add nodes to the queue if they are non-null

from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        dq = deque()
        dq.append(root)

        while dq:
            currentLevel = []
            dq_len = len(dq)

            for _ in range(dq_len):
                currentNode = dq.popleft()
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    dq.append(currentNode.left)
                if currentNode.right:
                    dq.append(currentNode.right)

            result.append(currentLevel)
        return result
