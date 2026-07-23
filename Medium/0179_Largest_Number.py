#Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        nums = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        nums.sort(key=cmp_to_key(compare))

        ans = "".join(nums)

        if ans[0] == "0":
            return "0"

        return ans