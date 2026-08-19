class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped_values = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            value2 = target - nums[i]
            if value2 in mapped_values and i != mapped_values[value2]:
                return [i, mapped_values[value2]]

