class Solution:
    def isPalindrome(self, x: int) -> bool:
        forward = x
        reverse = 0
        if x < 0 or (x > 0 and x%10 == 0):
            return False
        while x:
            digit = x % 10
            x = x // 10
            reverse = (reverse * 10) + digit
            
        if reverse == forward:
            return True
        else:
            return False
