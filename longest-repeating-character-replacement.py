"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.
"""

# my approach: keep a sliding window with a character counts dictionary, which tracks counts of the characters in the current window
# also keep a count of the character with the most counts, we've seen so far. as we expand our window, we can keep increasing the character
# counts in our dictionary. when we reach a count greater than the max counts, we can increase the max counts. we know that in our current window,
# everything except the maxCounts will be characters we need to replace. if at any point, we have more than k of those in the window, we will
# shrink our window and update our counts/maxcounts accordingly


def characterReplacement(self, s: str, k: int) -> int:
    n = len(s)
    left = 0
    bestLen = 0
    maxChars = 0
    charMap = {}
    for right in range(n):
        rightChar = s[right]
        if rightChar not in charMap:
            charMap[rightChar] = 0
        charMap[rightChar] += 1
        maxChars = max(maxChars, charMap[rightChar])
        if right - left + 1 - maxChars > k:
            charMap[s[left]] -= 1
            left += 1
        bestLen = max(bestLen, right - left + 1)
    return bestLen
