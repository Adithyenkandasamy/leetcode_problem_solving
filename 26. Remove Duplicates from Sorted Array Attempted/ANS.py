class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1  #checking from index 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:# for checking there is unique value or not
                nums[l]=nums[r]
                l += 1
        return l        