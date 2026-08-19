class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # get frequency dict for t
        tFreq = defaultdict(int)
        for ch in t:
            tFreq[ch] += 1
        

        visited = defaultdict(int)
        minWord = ""
        tailInd = -1

        for i in range(len(s)):
            ch = s[i]
            visited[ch] += 1
            if ch in tFreq:
                if tailInd == -1:
                    tailInd = i

                if visited[ch] > tFreq[ch] and s[tailInd] == ch:
                    #make word shorter (if tailInd is on same char), bring to next available char
                    visited[ch] -= 1
                    while tailInd < i:
                        tailInd += 1
                        if s[tailInd] in tFreq:
                            if visited[s[tailInd]] > tFreq[s[tailInd]]:
                                visited[s[tailInd]] -= 1
                                continue
                            break
                    print(ch, i, tailInd)

                matches = True
                for each in tFreq:
                    if visited[each] < tFreq[each]:
                        matches = False
                if matches:
                    minWord = minWord if len(minWord) < len(s[tailInd:i+1]) and minWord != "" else s[tailInd:i+1]
        return minWord                




