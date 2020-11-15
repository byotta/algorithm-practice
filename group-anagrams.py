"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

# my approach:
# create a character counts array for each word. then place it in a dictionary which maps from counts -> list of words. return the values
# of this dictionary at the end

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        countsToWords = {}
        for word in strs:
            tup = self.convertToCounts(word)
            if tup not in countsToWords:
                countsToWords[tup] = [word]
            else:
                countsToWords[tup].append(word)
        return countsToWords.values()
    def convertToCounts(self, s):
        counts = [0 for i in range(26)]
        for c in s:
            counts[ord(c) - ord('a')] += 1
        return tuple(counts)