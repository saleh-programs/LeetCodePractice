from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        sequences = {}
        maximum = 0
        for num in uniqueNums:
            if num in sequences:
                continue
            sequences[num] = 1
            if num - 1 not in uniqueNums:
                count = num + 1
                while (count in uniqueNums):
                    sequences[count] = 1
                    sequences[num] += 1
                    count += 1
            maximum = max(maximum, sequences[num])
        return maximum
