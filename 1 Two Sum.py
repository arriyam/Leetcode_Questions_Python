class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        book={}
        for i in range(len(nums)):
            book.update({nums[i]:i})
        for b in range(len(nums)):
            if target-nums[b] in book and b!=book[target-nums[b]]:
                return (b,book[target-nums[b]])