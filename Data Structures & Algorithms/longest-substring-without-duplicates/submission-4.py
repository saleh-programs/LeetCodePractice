from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0

        visited = set()
        longest = 0
        current = 0

        for i in range(len(s)):
            newChar = s[i]
            if newChar in visited:
                while newChar in visited:
                    visited.remove(s[l])
                    l += 1
                    current -= 1
                visited.add(newChar)
                current += 1

            else:
                visited.add(newChar)
                current += 1
                longest = max(longest, current)
        return longest