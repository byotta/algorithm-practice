"""
Given a non-empty array of integers, return the k most frequent elements.
"""

# my approach: simple python function call, using heap


from collections import Counter
from heapq import *


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        return nlargest(k, counts.keys(), key=lambda k: counts[k])
