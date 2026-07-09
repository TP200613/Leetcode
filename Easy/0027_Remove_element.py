#Remove all occurrences of a given value from an array in-place using the two-pointer technique and return the count of the remaining elements.
class Solution:
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k