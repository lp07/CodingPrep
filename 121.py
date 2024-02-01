# leetCode : 121 Best time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
# in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4], Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1], Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

class Solution:
    def maxProfit(self, prices):
        # Return 0 if there is no prices
        if not prices:
            return 0

        # Initialize a min_price, to the price on the first day
        min_price = prices[0]
        # set the max_profit to 0
        max_profit = 0

        for price in prices:
            # Update min_price, if lower price found
            min_price = min(min_price, price)
            # Update the max_profit, on basis of difference between price and min_price
            max_profit = max(max_profit, price - min_price)
        # Return the maximum profit achieved
        return max_profit

solution = Solution()
result1 = solution.maxProfit([7,1,5,3,6,4])
result2 = solution.maxProfit([7,6,4,3,1])
print(result1) # 5
print(result2) # 0


