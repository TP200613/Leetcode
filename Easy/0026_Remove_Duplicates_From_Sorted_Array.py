#Remove duplicate elements from a sorted array in-place so that each unique element appears only once, and return the count of unique elements.

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        w=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[w]=nums[r]
                w+=1
        return w

        