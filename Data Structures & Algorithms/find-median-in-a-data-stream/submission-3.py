class MedianFinder:
    # also not what I should do just testing
    def __init__(self):
        self.large = []
        self.small = []
    def addNum(self, num: int) -> None:
        if not self.small:
            self.small.append(-num)
            return
        if len(self.small) == len(self.large):
            if num <= -self.small[0]:
                heapq.heappush(self.small, -num)
            else:
                heapq.heappush(self.large, num)
                heapq.heappush(self.small, -heapq.heappop(self.large))
        else:
            if num <= -self.small[0]:
                heapq.heappush(self.small, -num)
                heapq.heappush(self.large, -heapq.heappop(self.small))
            else:
                heapq.heappush(self.large, num)


        
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        return -self.small[0]


