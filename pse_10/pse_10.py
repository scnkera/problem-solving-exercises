def max_profit(prices):
    
    profit = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]

    return profit