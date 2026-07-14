class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums))]
        counts = dict()
        
        for i in range(len(nums)):

            if counts.get(nums[i]) == None:
                counts[nums[i]] = 1

            else:
                counts[nums[i]] += 1
        
        
        for key, value in counts.items():
            freq[value - 1].append(key)

        top = []

        for i in range(len(freq) - 1, -1, -1):
            top.extend(freq[i])

            if len(top) >= k:
                return top
        
        return top


            




        