class KthLargest:
    # DAMMMMITTTTTTTT
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for i in range(len(nums)):
            self.addNormal(nums[i])

    def add(self, val: int) -> int:
        self.addNormal(val)
        if (len(self.heap) < self.k):
            return None
        else:
            print(self.heap)
            kRemoved = []
            for _ in range(self.k):
                x = self.getMax()
                kRemoved.append(x)
            for num in kRemoved:
                self.addNormal(num)
            print(self.heap)
            print(kRemoved[-1])
            return kRemoved[-1]
    def addNormal(self, val: int) -> None:
        self.heap.append(val)
        curri = len(self.heap) - 1
        while curri != 0 and val > self.heap[(curri-1)//2]:
            self.heap[curri], self.heap[(curri-1)//2] = self.heap[(curri-1)//2],self.heap[curri]
            curri = (curri-1) // 2
        
    def getMax(self) -> int:
        currMax = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        curri =  0
        while curri < len(self.heap):
            left = 2*curri + 1
            right = 2*curri + 2
            if left < len(self.heap) and right >= len(self.heap) and self.heap[left] > self.heap[curri]:
                self.heap[left], self.heap[curri]  = self.heap[curri], self.heap[left]
                curri = left
                break
            elif right < len(self.heap) and left >= len(self.heap) and self.heap[right] > self.heap[curri]:
                self.heap[right], self.heap[curri]  = self.heap[curri], self.heap[right]
                curri = right
                break
            elif right < len(self.heap) and left < len(self.heap):
                bigger = left if max(self.heap[left],self.heap[right]) == self.heap[left] else right 
                if self.heap[bigger] > self.heap[curri]:
                    self.heap[bigger], self.heap[curri]  = self.heap[curri], self.heap[bigger]
                    curri = bigger
                    continue
                else:
                    break
            else:
                break
        return currMax