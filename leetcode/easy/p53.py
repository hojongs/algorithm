"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
This is not an easy problem :)
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSubArray(nums, i) = maxSubArray(nums, i-1) > 0 ? maxSubArray(nums, i-1)+nums[i] : nums[i]
        # => maxSubArray(nums, i) = max(maxSubArray(nums, i-1)+nums[i], nums[i])
        # => maxSubArray(nums, i) = max(maxSubArray(nums, i-1), 0) + nums[i] (Only unless nums[i] < maxSubArray(nums, i-1) < 0)
        # dp[i]: maxSubArray(nums, i)...? 음수도 존재할 때는 의미가 조금 애매해짐
        # it can be single integer variable
        maxSum = nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            maxSum = max(maxSum, dp[i])
        return maxSum
