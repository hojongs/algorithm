"""
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

find the length of the longest increasing subsequence

임의 엘리먼트(인덱스)에서 the length of the longest increasing subsequence
= previous longest + (0 or 1)
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length

        for i in range(1, length):
            for k in range(i):
                if nums[k] < nums[i]:
                    if dp[k]+1 > dp[i]:
                        dp[i] = dp[k]+1

        return max(dp)


if __name__ == '__main__':
    print(Solution().lengthOfLIS([1, 2, 3, 4, 5]))  # 5
    print(Solution().lengthOfLIS([999, 1, 2, 3]))  # 3, nums[1]가 시작점
    print(Solution().lengthOfLIS([50, 51, 1, 2, 3]))  # 3, nums[2]가 시작점
    print(Solution().lengthOfLIS([1, 3, 5, 2, 3, 4, 5]))  # 5, nums[1]가 아닌 nums[4]를 포함해야 함
    print(Solution().lengthOfLIS([1, 2, 3, 4, 5, 2, 3]))  # 5, nums[5]가 아닌 nums[1]를 포함해야 함
    print(Solution().lengthOfLIS([10, 20, 15, 25, 18, 21, 23]))  # [10, ..., 15, ..., 18, 21, 23]
    print(Solution().lengthOfLIS([10, 20, 21, 23, 24, 25, 26, 27, 15, 25, 18, 21, 23]))  # [10, ..., 27]
