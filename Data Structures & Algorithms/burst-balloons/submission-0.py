class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        l = 1
        r = len(nums)

        nums = [1] + nums + [1]

        dp = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l,r)]

            dp[(l,r)] = 0
            for i in range(l, r + 1):
                c = nums[l-1] * nums[i] * nums[r + 1]
                c += dfs(l, i - 1) + dfs(i + 1, r)

                dp[(l,r)] = max(c, dp[(l,r)])
            
            return dp[(l,r)]
        
        return dfs(l, r)
        


