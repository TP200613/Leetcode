# Problem: Convert a Roman numeral into an integer.
class Solution(object):
    def romanToInt(self, s):
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        t= 0
        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                t -= a[s[i]]
            else:
                t += a[s[i]]

        return t

