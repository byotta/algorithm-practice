"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days 
you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

# my approach:
# using a stack, we will iterate the given temperature array backwards. we examine the stack for each T[i],
# popping off elements until we finally reach a higher temperature. once we reach this higher temp, we can edit res[i] to be the
# difference in indices of the higher - lower temperature. if we run out of temps in the stack, we know there is no higher temp after us,
# so we place 0 in the result, and we simply add ourself to the stack

# O(n) time | O(n) space (in the worst case where all values are increasing we fill the stack completely)


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0 for num in T]
        stack = []
        for i in reversed(range(len(T))):
            while len(stack) > 0 and stack[-1][1] <= T[i]:
                stack.pop()
            if len(stack) == 0:
                res[i] = 0
            else:
                res[i] = stack[-1][0] - i
            stack.append((i, T[i]))
        return res
