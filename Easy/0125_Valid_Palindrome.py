#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
class Solution(object):
    def isPalindrome(self, s):
        a=""
        for i in s:
            if i.isalnum()==True:
                a+=i.lower()
        if a[::-1]==a:
            return True
        elif s==" ":
            return True
        elif a[::-1]!=a:
            return False
        
        