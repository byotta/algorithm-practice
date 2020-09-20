"""
find the first occurrence of a value in an array, in log N time
"""
# my approach: standard binary search, however, instead of breaking/return when we find the target value,
# we will move our "right" pointer to right before the current mid. this will ensure that we also explore
# elements to the left of the current mid.

# O(log N) time | O(1) space


def first(arr, target):
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = left + (right - left) // 2
        if target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:  # found something equal to the target
            res = mid
            right = mid - 1
    return res
