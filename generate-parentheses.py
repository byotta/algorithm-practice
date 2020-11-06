"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

# my approach: pass in how many left and right parantheses you have remaining to place.
# if you have the same number of left and right to place, you can only place left parans (since right parans cant come first)
# recurse until the remaining left and remaining right are both = zero, meaning we are well-formed


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.compute(n, n, "", res)
        return res

    def compute(self, remainingLeft, remainingRight, curr, res):
        if remainingLeft == 0 == remainingRight:
            res.append(curr)
        elif remainingLeft == remainingRight:
            self.compute(remainingLeft - 1, remainingRight, curr + "(", res)
        else:
            if remainingLeft > 0:
                self.compute(remainingLeft - 1,
                             remainingRight, curr + "(", res)
            if remainingRight > 0:
                self.compute(remainingLeft, remainingRight -
                             1, curr + ")", res)
