class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #The bad solution
        result = []
        unique = set()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        unique.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        return [list(item) for item in unique]