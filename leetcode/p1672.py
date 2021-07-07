# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for account in accounts:
            richest = max(richest, sum(account))

        return richest


if __name__ == '__main__':
    print(Solution().maximumWealth([[1, 5], [7, 3], [3, 5]]))
