"""
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        e = 1
        result = 0
        for i in range(len(columnTitle)):
            c = columnTitle[-i-1]
            result += (ord(c) - 65 + 1) * e
            e *= 26
        return result


if __name__ == '__main__':
    print(Solution().titleToNumber('A'))
    print(Solution().titleToNumber('AB'))
