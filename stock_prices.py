def find_max_profit(prices):
    max = prices[1]-prices[0]
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j]-prices[i] > max:
                max = prices[j]-prices[i]
    return max


print find_max_profit([10, 11, 4, 8, 1, 2])
print find_max_profit([10, 9, 8, 7])
print find_max_profit([10, 7, 5, 8, 11, 9])
