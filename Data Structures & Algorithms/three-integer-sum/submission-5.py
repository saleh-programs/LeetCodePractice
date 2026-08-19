class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # this solution basically uses "2 sum with sorted input" n times
        result = []
        nums = sorted(nums)
        prev = None
        for i in range(len(nums)-2):
            if nums[i] == prev:
                continue
            prev = nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] > -nums[i]:
                    r -= 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    result.append([nums[i], nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result

        