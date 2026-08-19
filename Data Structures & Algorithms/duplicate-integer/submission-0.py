
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_set = set()
        for i in range(len(nums)):
            if nums[i] in dup_set:
                return True
            else:
                dup_set.add(nums[i])
        return False