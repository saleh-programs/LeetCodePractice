class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick solution
        negatedNums = [-n for n in nums]
        heapq.heapify(negatedNums)
        for _ in range(k-1):
            heapq.heappop(negatedNums)
        return heapq.heappop(negatedNums)*-1
