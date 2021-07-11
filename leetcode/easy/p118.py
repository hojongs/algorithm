"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

문제 정의 자체가 DP
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        rows = [[1], [1, 1]]
        # append next row
        for i in range(3, numRows + 1):
            # init the row
            row = [1] * i
            for k in range(1, i - 1):
                row[k] = rows[i - 2][k - 1] + rows[i - 2][k]

            rows.append(row)

        return rows


if __name__ == '__main__':
    print(Solution().generate(5))
