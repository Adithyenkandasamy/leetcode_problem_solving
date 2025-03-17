from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        right, left = len(height) - 1, 0
        max_area = 0  

        while left < right:
            capacity = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, capacity)  
            
            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1 

        return max_area
