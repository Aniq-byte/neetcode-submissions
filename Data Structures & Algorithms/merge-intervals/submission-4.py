class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        
        ranges = []

        for interval in intervals:

            if ranges == []:
                ranges.append(interval)
                start = interval[0]
                end = interval[1]
            else:
                if interval[0] > end:
                    ranges.append(interval)
                    start = interval[0]
                    end = interval[1]
                elif interval[0] <= end:
                    if interval[1] > end:
                        ranges.pop()
                        end = interval[1]
                        ranges.append([start, end])
        
        return ranges


        