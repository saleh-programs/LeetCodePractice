from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # garbage solution
        l = 0
        currStringMap = defaultdict(int)
        mostFreq = 0
        numReplacements = 0
        result = 0
        for i in range(len(s)):
            currStringMap[s[i]] += 1
            mostFreq = max(mostFreq, currStringMap[s[i]])
            numReplacements = ((i+1)-l) - mostFreq
            if numReplacements <= k:
                result = max(result, (i+1)-l)
            else:
                while numReplacements > k:
                    currStringMap[s[l]] -= 1
                    if currStringMap[s[l]] == 0:
                        del currStringMap[s[l]]
                    localMax = 0
                    for value in currStringMap.values():
                        localMax = max(localMax, value)
                    l += 1
                    numReplacements = ((i+1)-l) - localMax
        return result