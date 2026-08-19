from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_map = defaultdict(list)
        maximum = 0
        for num in nums:
            if num in seen_map:
                continue
            seen_map[num].append(num)
            if num - 1 in seen_map:
                seen_map[num].extend(seen_map[num - 1])
                seen_map[num - 1] = seen_map[num]
            if num + 1 in seen_map:
                seen_map[num].extend(seen_map[num + 1])
                seen_map[num + 1] = seen_map[num]
            for each in seen_map[num]:
                seen_map[each] = seen_map[num]

            maximum = max(maximum, len(seen_map[num]))
        return maximum
