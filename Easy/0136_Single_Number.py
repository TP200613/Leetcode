#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
class Solution(object):
    def singleNumber(self, nums):
        result = 0

        for i in nums:
            result ^= i

        return result