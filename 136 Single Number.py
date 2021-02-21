class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        left,right=0,1
        while left<len(nums):
            try:
                if nums[left]!=nums[right]:
                    try:
                        if nums[left]!=nums[left-1]:
                            return(nums[left])
                    except:
                        return(nums[left])
                left,right=left+1,right+1
            except:
                return(nums[len(nums)-1])