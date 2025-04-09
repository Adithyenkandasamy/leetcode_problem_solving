class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        for ans in s:
            if ans.isalnum():
                result += ans.lower()
        return result == result[::-1]

# For testing
print(isPalindrome("A man, a plan, a canal: Panama"))