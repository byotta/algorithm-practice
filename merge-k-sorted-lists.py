"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# my approach: classic approach - use a heap to capture all first elements of each list in the heap
# then keep popping the minimum from this heap and adding its next element
from heapq import *


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for root in lists:
            if root:
                heappush(heap, (root.val, root))

        head = ListNode(float('inf'))  # dummy node to simplify appends
        tail = head
        while heap:
            val, node = heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heappush(heap, (node.next.val, node.next))
        return head.next
