"""
Given a string s, return the longest palindromic substring in s.
"""

# my approach: key idea is to start from center, two cases: start from a letter (odd length string)
# and start between letters (even length string)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestString = ""
        bestLen = float('-inf')
        for i in range(len(s)):
            resOdd = self.helper(i, i, s)
            resEven = self.helper(i, i+1, s)

            resOddLen = resOdd[1] - resOdd[0] + 1
            resEvenLen = resEven[1] - resEven[0] + 1

            bestLeft, bestRight = -1, -1
            if resOddLen > resEvenLen:
                bestLeft, bestRight = resOdd[0], resOdd[1]
            else:
                bestLeft, bestRight = resEven[0], resEven[1]

            if bestRight - bestLeft + 1 > bestLen:
                bestLen = bestRight - bestLeft + 1
                bestString = s[bestLeft:bestRight+1]
        return bestString

    def helper(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return [left+1, right-1]
