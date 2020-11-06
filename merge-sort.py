def mergeSort(arr):
    left = 0
    right = len(arr) - 1
    if left >= right:
        return arr
    mid = left + (right - left) // 2
    a = mergeSort(arr[left:mid+1])
    b = mergeSort(arr[mid+1:right+1])
    res = merge(a, b)
    return res


def merge(a, b):
    res = []
    ptr1, ptr2 = 0, 0
    while ptr1 < len(a) and ptr2 < len(b):
        if a[ptr1] <= b[ptr2]:
            res.append(a[ptr1])
            ptr1 += 1
        else:
            res.append(b[ptr2])
            ptr2 += 1
    while ptr1 < len(a):
        res.append(a[ptr1])
        ptr1 += 1
    while ptr2 < len(b):
        res.append(b[ptr2])
        ptr2 += 1
    return res


a = [3, 2, 1, 4, 5, 6, 7, 8, 3, 2, 1, 5, 3, 22, 324, 3424]
a = mergeSort(a)
print(a)
