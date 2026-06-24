# Given two strings `s` and `t`, where `t` is formed by shuffling `s` and adding one extra character, return the added character.
class Solution(object):
    def findTheDifference(self, s, t):
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]

        return t[-1]
