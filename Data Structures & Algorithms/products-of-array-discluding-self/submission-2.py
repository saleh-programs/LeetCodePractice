class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        for i in range(0, len(nums)):
            if i == 0:
                prefix.append(nums[0])
                suffix.insert(0,nums[len(nums)-1])
                continue
            prefix.append(nums[i] * prefix[i-1])
            suffix.insert(0, nums[len(nums)- 1 - i] * suffix[0])
        prefix = [1] + prefix + [1]
        suffix = [1] + suffix + [1]

        result = []
        for i in range(1,len(nums)+1):
            result.append(prefix[i-1] * suffix[i+1])
        return result