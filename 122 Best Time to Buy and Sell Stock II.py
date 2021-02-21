class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit,i=0,1
        while i<len(nums):
            if nums[i]>nums[i-1]:
                profit+=nums[i]-nums[i-1]
            i+=1
        return(profit)