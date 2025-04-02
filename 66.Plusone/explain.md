```markdown
# Explanation of the `plusOne` Function

The `plusOne` function is designed to increment an integer represented as an array of digits by one. Here's a step-by-step explanation of the code:

## Code
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9: 
                digits[i] += 1
                return digits
            digits[i] = 0  

        return [1] + digits
```

## Explanation

1. **Iterating from the Last Digit**:
   - The `for` loop iterates over the list `digits` in reverse order, starting from the last digit (rightmost) and moving to the first digit (leftmost).

2. **Checking if the Current Digit is Less Than 9**:
   - If the current digit is less than 9, it can be incremented by 1 without causing a carry-over. The function updates the digit and immediately returns the modified list.

3. **Handling Carry-Over**:
   - If the current digit is 9, incrementing it would result in a carry-over. In this case, the digit is set to 0, and the loop continues to the next digit on the left.

4. **Adding a New Leading Digit**:
   - If the loop completes without returning (i.e., all digits were 9), it means the number was something like `999`. In this case, a new leading digit `1` is added to the front of the list, followed by all zeros (e.g., `999` becomes `1000`).

## Example

### Input:
```python
digits = [1, 2, 3]
```

### Execution:
- Start from the last digit (`3`), increment it to `4`, and return `[1, 2, 4]`.

### Input:
```python
digits = [9, 9, 9]
```

### Execution:
- Start from the last digit (`9`), set it to `0` (carry-over).
- Move to the next digit (`9`), set it to `0` (carry-over).
- Move to the first digit (`9`), set it to `0` (carry-over).
- Add a new leading `1`, resulting in `[1, 0, 0, 0]`.

## Complexity

- **Time Complexity**: `O(n)` where `n` is the number of digits, as the loop iterates through the list once.
- **Space Complexity**: `O(1)` additional space, as the modification is done in-place (except for the case where a new digit is added).

This function efficiently handles the problem of incrementing a number represented as an array of digits.
```