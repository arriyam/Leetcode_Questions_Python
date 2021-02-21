class Solution(object):
    def maxArea(self, height):
        left,right,water=0,len(height)-1,0
        while left<right:
            count=((len(height))-(left+1)-((len(height)-1)-right))*min(height[left],height[right])
            if count>water:
                water=count
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return(water)