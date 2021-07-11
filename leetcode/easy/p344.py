"""
344. Reverse String
https://leetcode.com/problems/reverse-string/
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return

        for i in range(len(s) // 2):
            s[i], s[-1 - i] = s[-1 - i], s[i]
        return
