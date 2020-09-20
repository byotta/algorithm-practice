"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
"""

# my approach: two pointer solution. left starts at 0, right starts at end of array. as we traverse, we want to greedily keep
# the higher of the two (height[left], height[right]). this gives us the best chance of finding the maximum area. we can iterate until
# left meets right, each time updating maxWater

# O(N) time | O(1) space


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = float('-inf')
        left, right = 0, len(height) - 1
        while left < right:
            minHeight = min(height[left], height[right])
            width = right - left
            currArea = width * minHeight
            maxWater = max(maxWater, currArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater
