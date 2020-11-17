"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""

# my approach. make two character inventory arrays. one for p, and one for the current window we are scanning through in s
# if both arrays are equal, add the left index of the window the result array


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # create pCounts
        pCounts = [0 for i in range(26)]
        for i in range(len(p)):
            c = p[i]
            pCounts[ord('a') - ord(c)] += 1

        res = []
        # create the window first
        counts = [0 for i in range(26)]
        left = 0
        for right in range(len(s)):
            c = s[right]
            counts[ord('a') - ord(c)] += 1
            if right - left + 1 > len(p):
                counts[ord('a') - ord(s[left])] -= 1
                left += 1
            if counts == pCounts:
                res.append(left)
        return res
