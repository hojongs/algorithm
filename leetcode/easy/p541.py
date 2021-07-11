"""
541. Reverse String II
https://leetcode.com/problems/reverse-string-ii/
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        for i in range(0, len(s), k * 2):
            if i + k <= len(s):
                for h in range(i + k, i, -1):
                    result += s[h - 1]
                for h in range(i + k, min(i + k * 2, len(s))):
                    result += s[h]
            else:
                for h in range(len(s), i, -1):
                    result += s[h - 1]
        return result
