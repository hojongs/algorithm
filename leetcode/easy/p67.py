"""
67. Add Binary
https://leetcode.com/problems/add-binary/
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = -1
        carry = 0
        result = ''
        max_len = max(len(a), len(b))
        while True:
            if max_len + i < 0:
                break

            my_sum = 0
            if len(a) + i >= 0 and a[i] == '1':
                my_sum += 1

            if len(b) + i >= 0 and b[i] == '1':
                my_sum += 1

            my_sum += carry

            if my_sum >= 2:
                my_sum -= 2
                carry = 1
            else:
                carry = 0

            result = str(my_sum) + result
            i -= 1

        if carry == 1:
            result = f'1{result}'

        return result
