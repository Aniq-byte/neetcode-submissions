class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [nums]
            else:
                return []

        nums.sort()

        sums = []

        for i in range(len(nums)):

            start = i + 1
            end = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = - nums[i]
            
            while start < end:
                if nums[start] + nums[end] == target:
                    if [nums[i], nums[start], nums[end]] not in sums:
                        sums.append([nums[i], nums[start], nums[end]])
                    start += 1
                elif nums[start] + nums[end] > target:
                     end -= 1
                else:
                    start += 1
        
        return sums






        