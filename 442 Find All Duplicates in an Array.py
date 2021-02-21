class Solution(object):
    def findDuplicates(self, nums):
        book,bob={},[]
        for i in range(len(nums)):
            if nums[i] in book:
                bob.append(nums[i])
            else:
                book.update({nums[i]:0})
        return(bob)