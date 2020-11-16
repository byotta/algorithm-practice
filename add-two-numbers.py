"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# my approach. iterate through the first list, build an int representation of the number. do the same for second list.
# add the two numbers together, then build a list representation of it.


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tens = 0
        curr = l1
        num1 = 0
        while curr:
            num1 = 10 ** tens * curr.val + num1
            curr = curr.next
            tens += 1
        curr = l2
        num2 = 0
        tens = 0
        while curr:
            num2 = 10 ** tens * curr.val + num2
            curr = curr.next
            tens += 1

        val = num1 + num2
        head = ListNode()
        tail = head
        if val == 0:
            return ListNode(0)
        while val > 0:
            digit = val % 10
            tail.next = ListNode(digit)
            tail = tail.next
            val //= 10
        return head.next
