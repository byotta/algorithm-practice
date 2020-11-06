"""
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.
"""
# my approach:
# keep taking the minimum between the fronts of each list


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr1 = l1
        curr2 = l2
        resStart, resEnd = None, None
        if curr1 and not curr2:
            return curr1
        if not curr1 and curr2:
            return curr2
        while curr1 and curr2:
            if not resStart:
                if curr1.val < curr2.val:
                    resStart = ListNode(curr1.val)
                    curr1 = curr1.next
                else:
                    resStart = ListNode(curr2.val)
                    curr2 = curr2.next
                resEnd = resStart
                continue
            if curr1.val < curr2.val:
                node = ListNode(curr1.val)
                resEnd.next = node
                curr1 = curr1.next
            else:
                node = ListNode(curr2.val)
                resEnd.next = node
                curr2 = curr2.next
            resEnd = resEnd.next
        while curr1:
            resEnd.next = ListNode(curr1.val)
            curr1 = curr1.next
            resEnd = resEnd.next
        while curr2:
            resEnd.next = ListNode(curr2.val)
            curr2 = curr2.next
            resEnd = resEnd.next
        return resStart
