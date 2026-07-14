class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        a = 0
        b = len(nums) - 1

        while a <= b:
            m = int((a+b)/2)

            if nums[m] == target:
                return m
            elif nums[m] < target:
                a = m + 1
            else:
                b = m - 1
            
        return -1
