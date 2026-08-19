class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = heapify(stones)
        while len(stones) > 1:
            x = stones[0]
            percolateDown(stones)
            y = stones[0]
            percolateDown(stones)
            print(stones,x,y)
            if x == y:
                continue
            if x < y:
                percolateUp(stones, y - x)
            else:
                percolateUp(stones, x - y)
        if stones:
            return stones[0]
        return 0


def heapify(nums:List[int]):
    heap =[]
    for i in range(len(nums)):
        percolateUp(heap, nums[i])
    return heap

def percolateUp(heap:List[int], val) -> List[int]:
    heap.append(val)
    current = len(heap)-1
    while current != 0 and heap[(current-1) // 2] < heap[current]:
        heap[(current-1) // 2], heap[current] = heap[current], heap[(current-1) // 2]
        current = (current-1) // 2
def percolateDown(heap:List[int]) -> List[int]:
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    heap.pop()
    current = 0
    while 2*current+1 < len(heap):
        left = heap[2*current+1]
        right = float("-inf")
        if 2*current + 2 < len(heap):
            right = heap[2*current+2]
        bigger = 2*current+1 if max(left, right) == left else 2*current + 2
        if heap[current] >= heap[bigger]:
            break
        heap[current], heap[bigger] = heap[bigger], heap[current]
        current = bigger