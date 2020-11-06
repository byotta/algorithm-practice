"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# my approach: one pass approach, keep two pointers, length k apart. when the first pointer reaches then end, we know the
# node to remove is at the tail pointer, so remove it


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        curr, tail = head, head
        while count < n:
            count += 1
            curr = curr.next
        if not curr:
            return head.next
        while curr.next:
            curr = curr.next
            tail = tail.next
        tail.next = tail.next.next
        return head
