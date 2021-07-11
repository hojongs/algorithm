"""
190. Reverse Bits
https://leetcode.com/problems/reverse-bits/
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f'{n:032b}'[::-1], 2)

    """
    Manual implementation version
    """
    # def reverseBits(self, n: int) -> int:
    #     result = ''
    #
    #     while n > 0:
    #         result += str(n % 2)
    #         n = n // 2
    #
    #     result += '0' * (32 - len(result))
    #
    #     return int(result, 2)


if __name__ == '__main__':
    print(Solution().reverseBits(43261596))
