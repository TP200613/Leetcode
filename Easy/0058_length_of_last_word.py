# Problem: Find the length of the last word in the given string.
class Solution(object):
    def lengthOfLastWord(self, s):
       a=s.split()
       c=len(a[-1])
       return c
          
        