"""
557. Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split()
        result = ''
        for my_str in strs:
            result += my_str[::-1] + ' '
        return result[:-1]
