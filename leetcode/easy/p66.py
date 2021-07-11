"""
66. Plus One
https://leetcode.com/problems/plus-one/

carry가 숨어있는 문제
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # plus one
        digits[-1] += 1
        i = len(digits) - 1

        # carry
        while i >= 0 and digits[i] == 10:
            digits[i] = 0

            if i == 0:
                return [1] + digits

            digits[i - 1] += 1
            i -= 1

        return digits
