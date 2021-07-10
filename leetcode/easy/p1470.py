"""
1470. Shuffle the Array
https://leetcode.com/problems/shuffle-the-array/
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = [0] * n * 2

        for i in range(n):
            shuffled[i * 2] = nums[i]
            shuffled[i * 2 + 1] = nums[n + i]

        return shuffled


if __name__ == '__main__':
    print(Solution().shuffle([2, 5, 1, 3, 4, 7], 3))
