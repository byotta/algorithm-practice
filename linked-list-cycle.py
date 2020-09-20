"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""

# my approach: fast and slow pointer. move fast 2 forward and slow 1 forward each iteration.
# by nature, if there is a cycle then the  two will meet at some point. if not, fast will each the
# end of the list and we can return False


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False
