from typing import List

def singleNumber(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res = res ^ num
        print(res)
    return res

x = singleNumber([1,2,2,3,3])    
# print(x)
