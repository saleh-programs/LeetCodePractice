from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in range(len(strs)):
            combination = [0] * 26

            for letter in strs[i]:
                combination[ord(letter) - ord("a")] += 1
            anagrams[",".join(str(c) for c in combination)].append(strs[i])
        return list(anagrams.values())
