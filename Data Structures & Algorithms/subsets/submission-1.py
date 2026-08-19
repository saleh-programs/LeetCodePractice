class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(2**len(nums)):
            curr = []
            binStr= f"{i:0{len(nums)}b}"
            for j in range(len(nums)):
                binStr[j] == "0" and curr.append(nums[j])
            result.append(curr)
        return result       