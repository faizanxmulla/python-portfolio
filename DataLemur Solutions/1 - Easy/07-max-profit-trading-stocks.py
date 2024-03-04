# 1 -> brute force solution

def max_profit(prices):
    max_profit = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            cur_profit = prices[j] - prices[i]
            if cur_profit > max_profit:
                max_profit = cur_profit
    return max_profit


# 2 -> clever solution

def max_profit(prices):
    min_price, max_profit = prices[0], 0

    for cur_price in prices[1:]:
        max_profit = max(max_profit, cur_price - min_price)
        min_price = min(min_price, cur_price)

    return max_profit
