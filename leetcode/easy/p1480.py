# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = [0] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                sums[0] = num
            else:
                sums[i] = sums[i-1] + num

        return sums


if __name__ == '__main__':
    print(Solution().runningSum([1, 1, 1, 1, 1]))
