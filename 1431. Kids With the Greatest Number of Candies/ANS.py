class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)
        result = []
        for i in candies:
            sum = i + extraCandies
            if sum >= maxcandies:
              result.append(True)
            else:
               result.append(False)  
        print(result)
        return result       
            