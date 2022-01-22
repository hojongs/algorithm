"""
1. Two Sum
https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dynamic = dict()

        for i in range(len(nums)):
            v = dynamic.get(target - nums[i])
            if v is not None:
                return [v, i]
            else:
                dynamic[nums[i]] = i


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3, 2, 4], 6))
