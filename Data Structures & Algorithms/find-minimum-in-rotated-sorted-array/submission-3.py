class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            middle = l + int((r - l) / 2)
            if nums[l] < nums[r]:
                return nums[l]
            elif nums[l] > nums[r]:
                if nums[l] > nums[middle]:
                    r = middle
                elif nums[l] <= nums[middle]:
                    l = middle + 1
        return nums[r]