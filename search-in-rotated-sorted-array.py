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
