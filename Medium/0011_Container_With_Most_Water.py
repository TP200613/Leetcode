# Find two lines that together with the x-axis form a container, such that the container contains the most water.
class Solution(object):
    def maxArea(self, height):
        lp=0
        rp=len(height)-1
        total_water=0

        while lp<rp:
            width=rp-lp
            current_height=min(height[lp],height[rp])
            current_area=width*current_height
            total_water=max(total_water,current_area)

            if height[lp]<height[rp]:
                lp+=1
            else:
                rp-=1
        return total_water

        