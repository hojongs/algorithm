# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0

        for i in range(len(nums) - 1):
            for k in range(len(nums) - i - 1):
                if nums[i] == nums[i + k + 1]:
                    cnt += 1

        return cnt


if __name__ == '__main__':
    print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
    print(Solution().numIdenticalPairs([1, 1, 1, 1]))
