class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        visited = set()
        longest = 0
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            count = 0
            while ((nums[i] + count) in numsSet):
                visited.add(nums[i] + count)
                count += 1
            longest = max(longest, count)
        return longest
