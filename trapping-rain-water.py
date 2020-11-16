"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # O(N) time O(N) space approach. in this approach, just built left max and right max for each index beforehand
        if not height:
            return 0
        n = len(height)
        leftMax = height[0]
        leftArray = [0 for i in range(n)]
        leftArray[0] = leftMax
        for i in range(1, n):
            leftArray[i] = max(leftArray[i-1], height[i])

        rightMax = height[n-1]
        rightArray = [0 for i in range(n)]
        rightArray[n-1] = rightMax
        for i in range(n-2, -1, -1):
            rightArray[i] = max(rightArray[i+1], height[i])

        total = 0
        for i in range(1, n-1):
            leftMax = leftArray[i]
            rightMax = rightArray[i]
            minimum = min(leftMax, rightMax)
            total += minimum - height[i]
        return total

        # brute force approach N^2. for each index i, compute the maximum to its left and the maximum to its right
        # find the min of those two max's, and subtract by the value at index i height. add that to the total
        # total = 0
        # n = len(height)
        # for i in range(1, n-1):
        #     maxLeft, maxRight = 0, 0
        #     curr = i
        #     while curr >= 0:
        #         maxLeft = max(maxLeft, height[curr])
        #         curr -= 1
        #     curr = i
        #     while curr < n:
        #         maxRight = max(maxRight, height[curr])
        #         curr += 1
        #     lowest = min(maxLeft, maxRight)
        #     total += lowest - height[i]
        # return total
