class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = dict();

        for i in range(len(nums)):
            if hash_map.get(nums[i]) == None:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] = hash_map.get(nums[i]) + 1

        for i in hash_map.values():
            if i > 1:
                return True
        
        return False
        
        