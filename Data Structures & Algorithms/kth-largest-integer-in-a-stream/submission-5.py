class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i in range(len(nums)):
            self.add(nums[i])
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            percolateUp(self.heap, val)
            return self.heap[0]
        if self.heap[0] >= val:
            return self.heap[0]
        percolateDown(self.heap)
        percolateUp(self.heap, val)
        return self.heap[0]

def percolateUp(heap:List[int], val) -> List[int]:
    heap.append(val)
    current = len(heap)-1
    while current != 0 and heap[(current-1) // 2] > heap[current]:
        heap[(current-1) // 2], heap[current] = heap[current], heap[(current-1) // 2]
        current = (current-1) // 2
def percolateDown(heap:List[int]) -> List[int]:
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    heap.pop()
    current = 0
    while 2*current+1 < len(heap):
        left = heap[2*current+1]
        right = float("inf")
        if 2*current + 2 < len(heap):
            right = heap[2*current+2]
        smaller = 2*current+1 if min(left, right) == left else 2*current + 2
        if heap[current] <= heap[smaller]:
            break
        heap[current], heap[smaller] = heap[smaller], heap[current]
        current = smaller
        
        

