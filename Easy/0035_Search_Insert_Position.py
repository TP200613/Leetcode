# Problem: Find the index of the target or its correct insert position in the sorted array.
class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)