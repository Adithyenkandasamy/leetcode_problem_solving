from typing import List

def sumOddLengthSubarrays(arr: List[int]) -> int:
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(i+1, n):
                  
            
arr = [1, 4, 2, 5, 3]
sumOddLengthSubarrays(arr)