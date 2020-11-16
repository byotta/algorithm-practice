"""
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
"""

# my approach: 3 pointers:
#   left: represents the next index where a 0 should go
#   index: the current index we are seeing
#   right: the next index where a 2 should go
# iterate through the array, and keep swapping with proper indices as we go


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        index = 0
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:  # 1
                index += 1
