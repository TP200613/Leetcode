# Problem: Convert a Roman numeral into an integer.
class Solution(object):
    def longestCommonPrefix(self, strs):
        p = strs[0]

        for s in strs[1:]:
            while not s.startswith(p):
                p= p[:-1]
