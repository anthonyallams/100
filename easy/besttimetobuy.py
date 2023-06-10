"""
Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


# SOLUTION 1: Brute force solution
# O(N^2) TIME AND O(1) SPACE
def maxProfit(prices: list[int]) -> int:
    """
    Goal is to buy low and sell high and derive the most profit

    Define the profit as 0 for a start and loop through the prices array
    Buy will be the price at i and sell is max of remaining arrays
    Determine if the difference in sell/buy price is bigger than the profit
    If so, set the profit to the difference of sell-buy else rinse and repeat for all values in the array
    """
    profit = 0
    for i in range(len(prices) - 1):
        buy = prices[i]
        sell = max(prices[i + 1 :])
        if sell - buy > profit:
            profit = sell - buy
    return profit


# OPTIMAL SOLUTION: One pass
# O(N) TIME AND O(1) SPACE
def maxProfit1(prices: list[int]) -> int:
    """
    Optimizations: Set the cheapest day to buy and define profit as 0
    Check the best price to sell daily-For every value in prices array, the sell price will become price at index i
    Check if profit we make by selling is better than previous profit-Profit is max of profit and difference in sell and buy
    Buy will be small as possible, being set as the minimum of initial buy price and subsequent values of price
    Return the maximum profit
    """
    profit = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        sell = prices[i]
        profit = max(profit, sell - buy)
        buy = min(buy, prices[i])
    return profit
