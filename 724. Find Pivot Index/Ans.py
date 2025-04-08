from typing import List

def pivotIndex(nums: List[int]) -> int:
        total = sum(nums)
        ltotal,rtotal = 0,0
        for i in range(len(nums)):
            rtotal = total -ltotal - nums[i]
            if ltotal == rtotal:
                return i
            ltotal += nums[i]
        return -1    


nums = [1,7,3,6,5,6]
print(pivotIndex(nums))