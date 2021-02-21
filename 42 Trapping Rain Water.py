class Solution:
    def trap(self, height: List[int]) -> int:
        right,left,total,level=len(height)-1,0,0,0
        while left<right:
            level=max(level,min(height[left],height[right]))
            total+=level-min(height[left],height[right])
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return(total)