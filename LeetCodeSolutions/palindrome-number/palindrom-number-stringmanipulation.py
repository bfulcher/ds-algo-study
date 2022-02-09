class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):
            return False
        if str(x)[::-1] == str(x):
            return True
        else:
            return False
