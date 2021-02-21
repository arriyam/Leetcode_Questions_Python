class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right, a = 0, len(nums) - 1, True
        while a == True:
            if nums[left] + nums[right] == target:
                return (left + 1, right + 1)
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1