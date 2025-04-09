from typing import List

def rearrangeArray(nums: List[int]) -> List[int]:
        positive = []
        negative = []
        result = []
    
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        n = len(positive)        
        for i in range(n):
            if i < n:
                result.append(positive[i])
                result.append(negative[i])
        return result 
print(rearrangeArray([1,2,3,-1,-2,-3]))
