from collections import deque
"""
Given a collection of distinct integers, return all possible permutations.
"""

# A classic math problem. Two approaches are covered: recursive backtracking, and iterative

# In the recursive approach, we keep a boolean array of the indices we have visited. We keep a current array
# for each recursive call. We add ourself to this current array, and mark our index as seen. Then we recursively
# call ourself, adding the next number in the list to the current list. When we notice that the current list size
# is the same as the original list size, then we know we have a valid permutation. Then we will "unchoose" by marking
# the index as not seen, and removing it from the current list


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper([], nums, res, [False for i in nums])
        return res

    def helper(self, curr, nums, res, seen):
        if len(curr) == len(nums):
            res.append(list(curr))
            return
        for i in range(len(nums)):
            if seen[i]:
                continue
            curr.append(nums[i])
            seen[i] = True
            self.helper(curr, nums, res, seen)
            curr.pop()
            seen[i] = False

# In the iterative approach, think of it as a BFS. We will create an empty array, then try to put the i'th element of the original
# array into every possible position of the previous arrays we composed.


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        permutations = deque()
        permutations.append([])  # base case, no elements
        for number in nums:
            # save the length of the queue since we will be appending to it
            n = len(permutations)
            for _ in range(n):
                oldPermutation = permutations.popleft()  # get the most recent permutation
                # place new element before and after every index
                for j in range(len(oldPermutation)+1):
                    # create new one, to avoid pass by reference
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(j, number)
                    if len(newPermutation) == len(nums):
                        res.append(newPermutation)
                    else:
                        permutations.append(newPermutation)
        return res
