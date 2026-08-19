class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #better solution
        visited_map = {}
        unique = set()
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                needed_value = -(nums[i] + nums[j])
                if needed_value in visited_map:
                    unique.add(tuple(sorted([nums[i],nums[j],needed_value])))
            visited_map[nums[i]] = i
        return [list(item) for item in unique]