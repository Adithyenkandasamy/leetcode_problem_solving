class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9: 
                digits[i] += 1
                return digits
            digits[i] = 0  

        return [1] + digits 
p=Solution()
print(p.plusOne([1,2,3]))  # Output: [1, 2, 4]  