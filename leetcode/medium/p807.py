"""
grid[r][c] = min(max(grid[r][:]), max(grid[:][c]))
"""
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        result = 0
        n = len(grid)
        rmax = []
        for r in range(n):
            rmax.append(max(grid[r]))
        cmax = []
        for c in range(n):
            cmax.append(max([grid[r][c] for r in range(n)]))
        for r in range(n):
            for c in range(n):
                result += min(rmax[r], cmax[c]) - grid[r][c]
        return result

    # def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    #     """
    #     Time complexity: O(n^3)
    #     Space complexity: O(1)
    #     """
    #     origin = sum([sum(row) for row in grid])
    #     n = len(grid)
    #     for r in range(n):
    #         for c in range(n):
    #             a = max(grid[r])
    #             b = 0
    #             for i in range(n):
    #                 b = max(b, grid[i][c])
    #             grid[r][c] = min(a, b)
    #
    #     return sum([sum(row) for row in grid]) - origin


if __name__ == '__main__':
    print(Solution().maxIncreaseKeepingSkyline(
        [
            [3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0]
        ]
    ))
