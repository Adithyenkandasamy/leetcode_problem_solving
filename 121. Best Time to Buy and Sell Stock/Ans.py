from typing import List

def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price<min_price:
            min_price = price
        else:
            profit = price - max_profit
            if profit > max_profit:
                max_profit = profit
                
    return max_profit  




arr = [7,6,4,3,1]
print(maxProfit(arr))
