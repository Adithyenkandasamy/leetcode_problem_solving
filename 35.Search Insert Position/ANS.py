from typing import List

def searchInsert(nums: List[int], target: int) -> int:
       if target in nums:
          if nums.index(target) >= 0:
            return nums.index(target)
       else:
           nums.append(target)
           nums.sort()
           return nums.index(target)
x = searchInsert([1,3,5,6], 5)          
print(x) # Output: 2