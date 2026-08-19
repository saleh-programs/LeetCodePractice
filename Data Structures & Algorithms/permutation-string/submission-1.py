from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        str1Freq = defaultdict(int)
        for ch in s1:
            str1Freq[ch] += 1
        
        visited = defaultdict(int)
        tailInd = 0
        for i in range(len(s2)):
            if s2[i] in str1Freq:
                visited[s2[i]] += 1
                if (i - tailInd + 1 == len(s1)):
                    if visited == str1Freq:
                        return True       
                    visited[s2[tailInd]] -= 1
                    tailInd += 1


            elif s2[i] not in str1Freq:
                tailInd = i + 1
                visited = defaultdict(int)
        return visited == str1Freq
                    