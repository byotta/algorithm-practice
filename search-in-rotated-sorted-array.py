"""
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.
"""

# my approach: do a simple binary search with some additional checks. we will be checking to see if a portion of the array is sorted.
# we will choose that portion, and see if the target falls within the range of that portion. if so, do a binary search in that portion.
# else, check the other portinon.


def search(self, arr: List[int], target: int) -> int:
    n = len(arr)
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target == arr[mid]:
            return mid
        # notice this = of the <= is very important to cover a case such as [3,1]
        # since we are using integer division, mid will bias towards left.
        # as such, when we have left = mid, we need to catch that case in the first branch
        if arr[left] <= arr[mid]:  # left side is sorted
            if arr[left] <= target < arr[mid]:  # target is within this range
                right = mid - 1
            else:  # need to examine the other half of the array
                left = mid + 1
        else:  # right side is sorted
            if arr[mid] < target <= arr[right]:  # target is within this range
                left = mid + 1
            else:  # examine other half
                right = mid - 1
    return -1
