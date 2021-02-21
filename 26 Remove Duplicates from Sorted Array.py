class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        place_holder, checker, a = 0, 1, True
        while a == True:
            try:
                if nums[place_holder] == nums[checker]:
                    nums.pop(place_holder)
                else:
                    place_holder, checker = place_holder + 1, checker + 1
                if checker == len(nums):
                    return (len(nums))
            except:
                try:
                    return (nums[0])
                except:
                    return (0)
