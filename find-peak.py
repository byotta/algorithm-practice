"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
"""

# my approach: rather than a standard O(N) array scan, we can perform a binary search approach,
# dropping half the array each time


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1

        # sanity checks
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[right-1] < nums[right]:
            return right

        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
