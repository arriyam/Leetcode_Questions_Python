class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        left,right,maxi=0,1,0
        while right<len(nums):
            if nums[left]>nums[right]:
                left=right
                right+=1
            else:
                total=nums[right]-nums[left]
                maxi=max(maxi,total)
                right+=1
        return(maxi)