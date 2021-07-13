"""
28. Implement strStr()
https://leetcode.com/problems/implement-strstr/

python is too slow
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
#         if haystack == "" and needle == "":
#             return 0

#         for i in range(len(haystack)):
#             flag = True
#             for k in range(len(needle)):
#                 if i+k >= len(haystack) or haystack[i+k] != needle[k]:
#                     flag = False
#                     break
#             if flag:
#                 return i
#         return -1
