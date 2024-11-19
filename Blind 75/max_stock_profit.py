# max stock profit brute force approach, using two for loops
# one starts from i=0 and another one starts from j=i+1
# calculate the profit and compare with the previous profit
# time complexity is O(n^2) and space complexity is O(1)

def max_profit_brute_force(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


# max stock profit better approach, one pass with running minimum
# use single pass through the array
# keep track of minimum price seen so far
# At each day, calculate the potential profit if you sold the stock at the current price and update the maximum profit.
# time complexity is O(n) and space complexity is O(1)

def max_profit_better(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


# max stock profit optimal solution, using Kadane's algorithm.
# This solution uses the same idea as the better solution but views it as a problem of finding the maximum subarray sum.
# Treat the difference prices[i] - prices[i-1] as a daily profit or loss.
# Use Kadane's Algorithm to find the maximum subarray sum of these differences.
# time complexity is O(n) and space complexity is O(1)

def max_profit_optimal(prices):
    max_profit = 0
    current_profit = 0

    for i in range(1, len(prices)):
        delta = prices[i] - prices[i-1]
        current_profit = max(0, current_profit + delta)
        max_profit = max(max_profit, current_profit)

    return max_profit