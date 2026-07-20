#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
class Solution(object):
    def searchRange(self, nums, target):
        l=[]
        sp=0
        ep=len(nums)-1
        if target not in nums:
            return [-1,-1]
        else:
            while sp<=ep:
                if nums[sp]==target:
                    l.append(sp)
                    sp+=1
                else:
                   sp+=1
        if len(l)==1:
            return [l[0],l[0]]
        else:
            return [l[0],l[-1]]