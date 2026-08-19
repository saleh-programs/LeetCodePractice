class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #GARBAGE SOLUTION: warning, this solution is so bad itll hurt your eyes i was just tired
        tLetterCount = {}
        for ch in t:
            tLetterCount[ch] = 1 + tLetterCount.get(ch,0)
        l = 0
        tLength = len(t)
        result = []
        for i in range(len(s)):

            if s[i] in tLetterCount:
                if tLetterCount[s[i]] <= 0 and s[i] == s[l]:
                    l+=1
                    while s[l] not in tLetterCount:
                        l += 1
                        if  s[l] in tLetterCount and tLetterCount[s[l]] < 0 and i != l:
                            tLetterCount[s[l]] += 1 
                            l += 1
                    tLetterCount[s[i]] += 1
                elif tLetterCount[s[i]] > 0:
                    tLength -= 1
                
                tLetterCount[s[i]] -= 1


                if tLength == 0:
                    result.append(s[l:i+1])
            else:
                if i == l:
                    l += 1
        minim = 100
        store_val = ""
        for i in range(len(result)):
            minim = min(minim, len(result[i]))
            if minim == len(result[i]):
                store_val = result[i]
        print(result)
        return store_val

                    