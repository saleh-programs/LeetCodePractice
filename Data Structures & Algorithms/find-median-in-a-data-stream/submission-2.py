class MedianFinder:
    # also not what I should do just testing
    def __init__(self):
        self.values = []
    def addNum(self, num: int) -> None:
        l = 0
        r = len(self.values)-1
        while l <= r:
            middle = l + (r-l)//2
            if self.values[middle] > num:
                r = middle - 1
            elif self.values[middle] < num:
                l = middle + 1
            else:
                l = middle
                break
        self.values.insert(l, num)
        
    def findMedian(self) -> float:
        middle = len(self.values) // 2
        if len(self.values) % 2 == 0:
            return (self.values[middle-1] + self.values[middle]) / 2
        return self.values[middle]

