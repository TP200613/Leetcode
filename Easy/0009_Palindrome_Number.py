# Problem: Check whether the given number is a palindrome.
class Solution(object):
    def isPalindrome(self, x):
        a=str(x)
        b=a[::-1]
        if a==b:
            return True
        else:
            return False