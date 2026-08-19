from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped_anagrams = defaultdict(list)
        for word in strs:
            char_map = {chr(i+97): 0 for i in range(26)}
            for ch in word:
                char_map[ch.lower()] += 1
            mapped_anagrams[tuple(char_map.values())].append(word)
        return mapped_anagrams.values()
