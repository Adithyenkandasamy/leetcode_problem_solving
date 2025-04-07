from typing import List

def maxProfit( prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                  profit += prices[i] - prices[i-1]
        return profit          
print(maxProfit([7,1,2,4,5,6]))

