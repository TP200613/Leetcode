# Problem: Check whether one string can be obtained by rotating another string.
class Solution(object):
    def rotateString(self, s, goal):
        return len(s) == len(goal) and goal in (s + s)