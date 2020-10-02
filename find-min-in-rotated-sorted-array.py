"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

# my approach: after some initial checks, begin a binary search. we will simply check the elements around the mid index, to
# see if the pivot is present. if so , we will return the element at the pivot since it will be the min
# otherwise, we will look at the unsorted portion of the array, since the pivot will occur there and thus our min


def findMin(self, arr: List[int]) -> int:
    n = len(arr)
    if n < 1:
        return -1
    if n == 1:
        return arr[0]
    if arr[0] < arr[n-1]:
        return arr[0]
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right-left) // 2
        if mid > 0 and arr[mid-1] > arr[mid]:
            return arr[mid]
        if mid < n - 1 and arr[mid] > arr[mid+1]:
            return arr[mid+1]
        if arr[left] <= arr[mid]:  # this portion is sorted, thus the real pivot will be to the right
            left = mid + 1
        else:
            right = mid - 1
    return -1
