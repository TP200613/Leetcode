# Used string reversal to reverse an integer while handling negative numbers and ensuring the result stays within the 32-bit signed integer limit.
class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_str = str(x)[::-1]
        reversed_int = int(reversed_str) * sign
        if reversed_int < -2147483648 or reversed_int > 2147483647:
            return 0
            
        return reversed_int