from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for i in range(len(strs)):
            letter_count = defaultdict(int)
            for letter in strs[i]:
                letter_count[letter] += 1
            word = []
            for key in letter_count:
                word.append(f'{key}{letter_count[key]}')
            word.sort()
            newKey = "".join(word)
            anagrams[newKey].append(strs[i])
        return list(anagrams.values())
            

