class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_number = str(x)
        if str_number == str_number[::-1]:
            return True
        else:
            return False

# Test cases
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121))  # Output: False
print(solution.isPalindrome(10))   # Output: False
