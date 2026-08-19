class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while (l < r):
            middle = l+((r-l)//2)

            if (nums[middle] > nums[r]):
                l = middle + 1
            else:
                r = middle
        startVal = l
        if nums[-1] < target:
            l,r = 0, startVal - 1
        else:
            l,r = startVal, len(nums)-1

        while (l <= r):
            middle = l+((r-l)//2)

            if (nums[middle] == target):
                return middle
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return -1

