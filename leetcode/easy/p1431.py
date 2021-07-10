# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        checks = [False] * len(candies)
        for i, candy in enumerate(candies):
            checks[i] = candy + extraCandies >= maximum

        return checks


if __name__ == '__main__':
    print(Solution().kidsWithCandies([2, 3, 5, 1, 3], 3))
