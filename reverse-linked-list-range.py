"""
Reverse a linked list from position m to n. Do it in one-pass.
"""

# my approach: similar to normal linked list. just keep some pointers which find the desired node


class Solution(object):
    def reverseBetween(self, head, p, q):
        if head is None or head.next is None:
            return head
        beforeBeg, beginning = None, head
        for _ in range(p-1):
            beforeBeg = beginning
            beginning = beginning.next

        end, afterEnd = head, None
        for _ in range(q-1):
            end = end.next
        afterEnd = end.next

        prev, curr = afterEnd, beginning

        while curr is not afterEnd:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        if beforeBeg is None:
            head = prev
        else:
            beforeBeg.next = prev
        return head
