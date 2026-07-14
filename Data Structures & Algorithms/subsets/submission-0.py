class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        out = []

        temp = []

        def dfs(i: int):
            if i == len(nums):
                out.append(temp.copy())
                return
            
            temp.append(nums[i])
            dfs(i+1)

            temp.pop()
            dfs(i+1)
        
        dfs(0)

        return out