from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        queue = deque()
        result = []


        for r in range(len(nums)):
            nextInWindow = nums[r]

            if not queue:
                queue.append(r)
                continue

            if queue[0] <= r - k:
                queue.popleft()
            if nextInWindow >= nums[queue[-1]]:
                while queue and nextInWindow >= nums[queue[-1]]:
                    queue.pop()
                queue.append(r)
            else:
                queue.append(r)
            if r + 1 >= k:
                result.append(nums[queue[0]])
        return result