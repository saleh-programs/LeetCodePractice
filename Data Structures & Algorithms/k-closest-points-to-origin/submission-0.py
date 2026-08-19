class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i, point in enumerate(points):
            heapq.heappush(maxHeap,(-math.sqrt(point[0]**2 + point[1]**2), i))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        result = []
        for _ in range(len(maxHeap)):
            result.append(points[heapq.heappop(maxHeap)[1]])
        return result