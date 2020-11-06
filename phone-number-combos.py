"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

# my approach:
# create of the map of the digit to letter pairings. then for each number, iterate through the possible letters,
# and add that to the result map


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if not digits:
            return res
        letterMap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        self.compute(digits, 0, "", res, letterMap)
        return res

    def compute(self, digits, currIndex, curr, res, letterMap):
        if currIndex >= len(digits):
            res.append(curr)
            return
        currDigit = int(digits[currIndex])
        letters = letterMap[currDigit]
        for letter in letters:
            self.compute(digits, currIndex + 1, curr + letter, res, letterMap)
