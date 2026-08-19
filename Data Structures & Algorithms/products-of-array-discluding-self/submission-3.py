class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # my simple solution
        prefix = []
        suffix = []
        result = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[0])
                suffix.insert(0, nums[-1])
                continue
            prefix.append(prefix[-1] * nums[i])
            suffix.insert(0, suffix[0] * nums[len(nums)-1-i])
        prefix = [1] + prefix + [1]
        suffix = [1] + suffix + [1]
        return [prefix[i-1] * suffix[i+1] for i in range(1,len(nums)+1)]