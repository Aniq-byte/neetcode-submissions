import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = nums
        heapq.heapify(self.pq)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        # print(heapq.nlargest(self.k, self.pq))
        return heapq.nlargest(self.k, self.pq)[self.k - 1]
        # print(self.pq)
        # return self.pq[-self.k]

        
