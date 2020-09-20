"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
"""

# my approach: kadane's algorithm: at each i, consider resetting the current contiguous sum to simply nums[i]
# O(N) time | O(1) space


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bestSum = float('-inf')
        currSum = 0
        i = 0
        while i < len(nums):
            potentialSum = currSum + nums[i]
            newSum = nums[i]
            if newSum > potentialSum:
                currSum = newSum
            else:
                currSum = potentialSum
            i += 1
            bestSum = max(bestSum, currSum)
        return bestSum
