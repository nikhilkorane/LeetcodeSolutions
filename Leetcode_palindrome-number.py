class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Check if number is -ve then always false 
        if x<0:
            return False
        #Check if reverse number is matching then True
        elif x == int(str(x)[::-1]):
            return True
        else:
            return False
