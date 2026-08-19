class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visited = {}
        for i in range(len(nums)):
            visited[nums[i]] = i

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in visited and i != visited[needed]:
                return [min(visited[needed], i), max(visited[needed],i)]

        return [-1,-1]