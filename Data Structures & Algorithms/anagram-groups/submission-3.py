from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)
        for word in strs:
            lettersFreq = [0] * 26
            for ch in word:
                lettersFreq[ord(ch) - ord('a')] += 1
            anagramGroups[tuple(lettersFreq)].append(word)
        return list(anagramGroups.values())