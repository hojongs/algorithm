"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        col_i = 0
        while True:
            if col_i >= len(strs[0]):
                return strs[0][:col_i]

            prefix = strs[0][col_i]
            for row_i, str in enumerate(strs):
                if col_i >= len(str):
                    return str[:col_i + 1]

                if str[col_i] != prefix:
                    return str[:col_i]
            col_i += 1


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["fl", "flight", "flight"]))
    print(Solution().longestCommonPrefix(["flower", "fl", "flight"]))
    print(Solution().longestCommonPrefix(["a"]))
