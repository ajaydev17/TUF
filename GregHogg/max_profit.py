# max profit stock problem using one loop
# time complexity O(n) and space complexity O(1)

def max_profit_optimized(prices):
    # initialize first index and max_profit
    left = 0
    max_profit = 0

    for index in range(1, len(prices)):
        # calculate the profit
        profit = prices[index] - prices[left]

        # update max_profit if profit is greater than zero else update the left pointer
        if profit > 0:
            max_profit = max(max_profit, profit)
        else:
            left = index