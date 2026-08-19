class MedianFinder:
    # wrong i know just seeing edges
    def __init__(self):
        self.values = []
    def addNum(self, num: int) -> None:
        self.values.append(num)
        self.values.sort()
    def findMedian(self) -> float:
        middle = len(self.values) // 2
        if len(self.values) % 2 == 0:
            return (self.values[middle-1] + self.values[middle]) / 2
        return self.values[middle]

