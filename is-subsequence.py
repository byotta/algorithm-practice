"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ace" is a subsequence of "abcde" while "aec" is not).
"""

# my approach: two pointer solution. iterate through each string with a different pointer. if they are both the same at the pointers'
# position, increment both. else just increment the one in string t. if we ever reach a scenario where the pointer of s is out of bounds,
# then we know we iterated through the whole string and we can return true. but if  we finish the second string and we havent finished
# the first string, then we must return false.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s):
            while j < len(t):
                if i >= len(s):
                    return True
                if s[i] == t[j]:
                    i += 1
                j += 1
            if i < len(s):
                return False
        return True
