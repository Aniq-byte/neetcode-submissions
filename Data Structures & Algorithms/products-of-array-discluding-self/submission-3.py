class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [1] * n

        pfx = 1
        for i in range(n):
            result[i] = pfx 
            pfx *= nums[i]
        
        sfx = 1
        for i in range(n-1, -1, -1):
            result[i] *= sfx
            sfx *= nums[i]

        return result
        