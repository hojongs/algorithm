"""
1365. How Many Numbers Are Smaller Than the Current Number
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/discuss/524996/JAVA-beats-100-O(n)
        Core concept: 점화식으로 표현, n 이하 수의 개수 = n-1의 개수 + n-1 이하 수의 개수
        Time complexity: O(n)

        cnts[i]: i를 포함한 i 이하 수의 개수
        Input: 8,1,2,2,3
        1. cnts = [0,1,2,1,0,0,0,0,1]
        2. cnts = [0,1,3,4,4,4,4,4,5]
        """
        cnts = [0] * 100
        for n in nums:
            cnts[n] += 1
        for i in range(1, len(cnts)):
            cnts[i] += cnts[i-1]
        res = [None] * len(nums)
        for i, n in enumerate(nums):
            res[i] = cnts[n - 1]
        return res
