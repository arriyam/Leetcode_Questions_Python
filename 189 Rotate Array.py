class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0,nums[len(nums)-1])
            nums.pop(len(nums)-1)