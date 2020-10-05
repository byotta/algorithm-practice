"""
Given a string s, find the length of the longest substring without repeating characters.
"""

# my approach: sliding window. maintain two pointers, left and right. keep adding s[right] into the currentSet. if s[right] is in
# the set, then we need to move up the left pointer until we remove s[right]. keep a max count variable to return and update as we go


def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    left = 0
    currSet = set()
    best = float('-inf')
    for right in range(n):
        if s[right] in currSet:
            while s[left] != s[right]:
                currSet.remove(s[left])
                left += 1
            currSet.remove(s[left])
            left += 1
        currSet.add(s[right])
        best = max(best, right-left+1)
    return best
