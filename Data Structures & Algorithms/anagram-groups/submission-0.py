from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = defaultdict(list)
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            sorted_map[sorted_word].append(strs[i])
        return [wrd_list.copy() for wrd_list in sorted_map.values()]
