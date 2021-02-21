class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        try:
            left_pointer=0
            for a in range(len(nums)):
                if nums[left_pointer]!=0:
                    left_pointer+=1
                if nums[left_pointer]==0:
                    nums.pop(left_pointer)
                    nums.append(0)
            return(nums)
        except:
                return(nums)