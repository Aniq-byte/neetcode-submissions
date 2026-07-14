class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        out = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                _, popped = stack.pop()
                out[popped] = i - popped
            
            stack.append([temp, i])
        
        return out