"""
Given a collection of intervals, merge all overlapping intervals.
"""

# my approach: sort intervals in order of increasing start time. then going left to right,
# begin the merging process until there are no more intervals to process.

# O(N*logN) time | O(N) space for sorting (Python's Timsort)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n < 2:
            return intervals
        
        res = []
        
        intervals.sort()
        first = intervals.pop(0)
        start, end = first[0], first[1]
        
        while intervals:
            currentInterval = intervals.pop(0)
            if currentInterval[0] <= end:
                end = max(end, currentInterval[1])
            else:
                res.append([start, end])
                start, end = currentInterval[0], currentInterval[1]
        res.append([start, end])
        return res