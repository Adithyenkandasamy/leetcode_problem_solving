from typing import List

def minOperations(nums: List[int], k: int) -> int:
        all_equal = True
        for num in nums:
            if num != k:
                all_equal = False
                break

        if all_equal:
            return 0

        for num in nums:
            if num < k:
                return -1

        unique_greater = []
        for num in nums:
            if num > k and num not in unique_greater:
                unique_greater.append(num)

        return len(unique_greater)  

nums = [2,5,5,4,5]
k = 2     
print(minOperations(nums, k))  # Output: 2        
