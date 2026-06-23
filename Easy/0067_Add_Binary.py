# Problem: Add two binary strings and return the result as a binary string.
class Solution(object):
    def addBinary(self, a, b):
        s = int(a, 2) + int(b, 2)
        return bin(s)[2:]