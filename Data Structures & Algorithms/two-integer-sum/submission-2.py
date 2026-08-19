class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapsupport = {}

        for i in range(len(nums)):
            needed_value = target - nums[i]
            if needed_value in mapsupport:
                return [mapsupport[needed_value], i]
            mapsupport[nums[i]] = i
        return []