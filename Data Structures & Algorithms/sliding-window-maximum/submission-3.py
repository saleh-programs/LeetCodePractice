from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        result = []
        window = deque()
        r = 0
        while r < len(nums):
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            window.append(r)
            if window[0] < r-k+1:
                window.popleft()
            if r+1 >= k:
                result.append(nums[window[0]])
            r+=1
        return result