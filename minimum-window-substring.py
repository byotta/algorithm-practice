"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
"""

# my approach: sliding window. keep a count of the number of characters that are "correctly matched to T". once we have all of the characters
# encaptured by T in our current window, then we can seek to decrease the size of the window accordingly.

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounts = Counter(t)
        n = len(s)
        bestWindowIndices = (0, 0)
        left = 0
        numCorrect = 0
        sCounts = {}
        minLen = float("inf")
        for right in range(n):
            rightChar = s[right]
            if rightChar not in sCounts:
                sCounts[rightChar] = 0
            sCounts[rightChar] += 1
            if rightChar in tCounts and sCounts[rightChar] == tCounts[rightChar]:
                numCorrect += 1
            while numCorrect == len(tCounts):
                if right - left + 1 < minLen:
                    bestWindowIndices = (left, right+1)
                    minLen = right - left + 1
                leftChar = s[left]
                sCounts[leftChar] -= 1
                left += 1
                if leftChar in tCounts and sCounts[leftChar] < tCounts[leftChar]:
                    numCorrect -= 1
        return s[bestWindowIndices[0]:bestWindowIndices[1]] if minLen != float("inf") else ""
