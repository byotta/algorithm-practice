"""
A linked list is given such that each node contains an additional random pointer which could point to 
any node in the list or null.

Return a deep copy of the list.
"""
# my approach: simple hashmap copy. O(N) time | O(N) space


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    # for debugging purposes
    def __str__(self):
        return str(self.val) if self else "None"


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        # first create mappings
        table = {}
        curr = head
        while curr:
            table[curr] = Node(curr.val)
            curr = curr.next
        # mappings should be complete
        # now just add the references
        curr = head
        newHead = table[head]
        cloneCurr = newHead
        while curr:
            if curr.next:
                cloneCurr.next = table[curr.next]
            if curr.random:
                cloneCurr.random = table[curr.random]
            curr = curr.next
            cloneCurr = cloneCurr.next
        return newHead

# very non-ideal way to provide a test case
# sol = Solution()
# first = Node(7)
# second = Node(13)
# third = Node(11)
# fourth = Node(10)
# fifth = Node(1)
# first.next = second
# second.next = third
# third.next = fourth
# fourth.next = fifth
# second.random = first
# third.random = fifth
# fourth.random = third
# fifth.random = first
# sol.copyRandomList(first)
