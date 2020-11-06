"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""

# my approach: add the empty set to our initial result. then for each number in the array, add it to all the pre-existing
# subsets in the result list. we will keep building this up, in a breadth-first fashion


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            n = len(res)
            for i in range(n):
                newSubset = res[i] + [num]
                res.append(newSubset)
        return res
