from typing import List
  
def minimumOperations( nums: List[int]) -> int:
    count = 0
    while len(nums) > len(set(nums)):
        nums = nums[3:]
        count += 1
    return count

x = minimumOperations([1,1,2,3,4,5])
print(x)
 
