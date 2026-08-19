from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for ch in s:
            s_dict[ch] += 1
        for ch in t:
            t_dict[ch] += 1

        return s_dict == t_dict