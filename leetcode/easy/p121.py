# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1. Brute force: Time limit exceeded
        Time complexity: O(N^2)
        Space complexity: O(1)
        loop for each day to buy in all prices
        inner-loop for each to sell in (next day ~ last day)
        compare sell - buy and save max value
        return max value

        best = 0
        for i in range(len(prices)):
            for k in range(i+1, len(prices)):
                buy = prices[i]
                sell = prices[k]
                if sell - buy > best:
                    best = sell - buy
        return best

        2. DP: Accepted
        Time complexity: O(N)
        Space complexity: O(N)
        loop the prices backwards
        mark the best price to sell for each day (need a list)
        - compare current price and previous marked price
        loop the prices
        compare the buy price - marked price (best to sell price) and save the max value
        return the total max value

        More simplify: mark the max profit instead of best price to sell

        3. Min price and Max profit
        Time complexity: O(N)
        Space complexity: O(1)
        """
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            if max_profit < prices[i] - min_price:
                max_profit = prices[i] - min_price
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
