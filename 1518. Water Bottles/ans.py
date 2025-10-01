class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles 
        while numBottles>=numExchange:
            numBottles -= numExchange
            numBottles += 1

            print(numBottles)
            total+=1
        return total

S= Solution()
x = S.numWaterBottles(9,3)
print(x)

