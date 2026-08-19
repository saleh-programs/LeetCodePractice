class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        currMax = nums[0]
        minVal = nums[0]
        while (l <= r):
            middle = l+((r-l)//2)

            if (nums[middle] >= currMax):
                currMax = nums[middle]
                l = middle + 1
            else:
                minVal = nums[middle]
                r = middle - 1
        return minVal