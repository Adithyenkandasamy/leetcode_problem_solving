from typing import List

num =""

def getConcatenation(nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums 

arr = [1, 2, 1]
print(getConcatenation(arr))        