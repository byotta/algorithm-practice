"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""
# my approach: scan through the list of intervals. pass over elements which have an end time before the start time of the new interval
# these intervals do not need to be merged. once we arrive at an interval whose end time is either = or > the start time of our new interval,
# we know we need to perform a merge. as such, perform the merging operation on all relevant intervals.  i.e, those whose start times are <=
# the end time of our new interval. finally, append this new merged interval onto the result, and add the last intervals on the list

# O(N) time [scan through list once] | O(N) space [result list]


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res
