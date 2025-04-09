nums = [2,3,1,1,4]


from typing import List

def jump(nums: List[int]) -> int:
        sum, count, a = 0, 0, 0
        n = len(nums)
        for i in range(n - 1):
            sum = max(sum, nums[i] + i)
            if i == a:
                a = sum
                count += 1
        return count

print(jump(nums))