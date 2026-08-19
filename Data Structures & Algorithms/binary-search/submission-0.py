class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r  = len(nums)-1
        while (l <= r):
            middle = l + int((r - l) / 2)

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l += 1
            else:
                r -= 1
        return -1