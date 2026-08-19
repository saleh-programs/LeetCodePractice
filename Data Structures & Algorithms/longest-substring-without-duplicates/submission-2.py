class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        currSequence = set()
        maxLength = 0
        for i in range(len(s)):
            while s[i] in currSequence and l != i:
                currSequence.remove(s[l])
                l += 1                 
            currSequence.add(s[i])
            maxLength = max(maxLength, (i+1) - l)
        return maxLength
