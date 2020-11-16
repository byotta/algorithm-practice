"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""
# my approach: find the length of both lists. then "equalize" the starting points of both lists by incrementing
# the head of the longer list to be at the same position where the other lists starts. now that the two heads are
# aligned, we can increment both until we find the intersection node. if one turns null, then there is not an intersection


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA and headB:
            return None
        if headA and not headB:
            return None
        if not headA and not headB:
            return None
        len1 = 0
        curr = headA
        while curr:
            len1 += 1
            curr = curr.next

        len2 = 0
        curr = headB
        while curr:
            len2 += 1
            curr = curr.next
        offset = len2 - len1  # if negative, then list1 was bigger
        newHeadA = None
        newHeadB = None
        if offset < 0:
            curr = headA
            while offset < 0:
                curr = curr.next
                offset += 1
            newHeadA = curr
        elif offset > 0:
            curr = headB
            while offset > 0:
                curr = curr.next
                offset -= 1
            newHeadB = curr
        currA = headA if not newHeadA else newHeadA
        currB = headB if not newHeadB else newHeadB
        while currA and currB and not currA is currB:
            currA = currA.next
            currB = currB.next
        if not currA:
            return None
        return currA
