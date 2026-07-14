class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # point one to the first number, and one to the last number
        # sum pointers and if it's bigger than target move right pointer down but if less than move left up

        first = 0
        last = len(numbers) - 1

        while first < last:

            if target == (numbers[first] + numbers[last]):
                return [first + 1, last + 1]
            elif target < (numbers[first] + numbers[last]):
                last -= 1
            else:
                first += 1
        
        return [numbers[first], numbers[last]]

        

        