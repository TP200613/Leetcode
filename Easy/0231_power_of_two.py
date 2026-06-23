# Problem: Check whether the given number is a power of two.
class Solution(object):
    def isPowerOfTwo(self, n):
        a=0
        while 2**a <= n:
            if 2**a==n:
                return True
            a+=1
        return False