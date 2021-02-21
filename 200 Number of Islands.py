class Solution:
    def numIslands(self, nums: List[List[str]]) -> int:
        total=0
        def dfs(nums,y,x):
            if x<0 or y<0 or x>=len(nums[0]) or y>=len(nums) or nums[y][x]!="1":
                return
            nums[y][x]="2"
            dfs(nums,y+1,x)
            dfs(nums,y-1,x)
            dfs(nums,y,x+1)
            dfs(nums,y,x-1)
        for y in range(len(nums)):
            for x in range(len(nums[0])):
                if nums[y][x]=="1":
                    dfs(nums,y,x)
                    total+=1
        return (total)