"""
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

118 정답 코드 재활용
시간되면 O(rowIndex)로 풀어보자
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        prev_row = [1, 1]
        # append next row
        for i in range(3, rowIndex + 2):
            # init the row
            row = [1] * i
            for k in range(1, i - 1):
                row[k] = prev_row[k - 1] + prev_row[k]

            prev_row = row

        return prev_row


if __name__ == '__main__':
    print(Solution().getRow(5))
