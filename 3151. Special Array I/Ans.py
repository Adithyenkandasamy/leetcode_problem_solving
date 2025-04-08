from typing import List

def isArraySpecial( nums: List[int]) -> bool:
        for i in range(1,len(nums)):
            if nums[i] & 1 == nums[i-1] & 1:
                return False
        return True       

print(isArraySpecial([1,2,3,4,5])) # True 