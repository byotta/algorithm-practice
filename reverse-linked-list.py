"""
Reverse a singly linked list.
"""

# my approach: keep a "prev" pointer which is the head of the reversed version of the linked list.
# keep passing references from curr, onto prev.


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        prev, curr = None, head

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
