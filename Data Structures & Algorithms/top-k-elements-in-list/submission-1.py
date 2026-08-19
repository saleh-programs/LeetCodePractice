from collections import defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        freq_map = defaultdict(int)
        k_list = []
        for i in range(len(nums)):
            freq_map[nums[i]] += 1
        for key, value in freq_map.items():
            if len(k_list) < k:
                k_list.append(key)
            else:
                minimum = 0
                for i in range(len(k_list)):
                    if freq_map[k_list[minimum]] > freq_map[k_list[i]]:
                        minimum = i
                if value > freq_map[k_list[minimum]]:
                    k_list[minimum] = key
        return k_list

