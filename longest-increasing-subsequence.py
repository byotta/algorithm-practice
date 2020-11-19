"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements 
without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""

# approach: keep a memo array, which will indicate the length of longest increasing subarray which ends at
# at i. iterate two pointer, one i one j, j will iterate up till i. at every iteration of j, if j's val
# is less than i's val, then it is a contender to be an increasing subsequence. we will see if its advantageous
# to append i to this array, or keep i's old sequence length (as indicated by max) simply return the max
# at the end of these loops


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[j] + 1, memo[i])
        return max(memo)
