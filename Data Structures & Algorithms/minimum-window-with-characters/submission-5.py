class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tChars = {}
        needed = 0
        for ch in t:
            if ch not in tChars:
                tChars[ch] = 0
            tChars[ch] += 1
            needed += 1
        have = 0

        window = defaultdict(int)
        shortest = ["", float("inf")]
        l = 0

        for r, ch in enumerate(s):
            if ch not in tChars:
                continue
            window[ch] += 1
            if have == 0:
                l = r
            if window[ch] <= tChars[ch] and have < needed:
                have += 1
            if have >= needed:
                if window[s[l]] > tChars[s[l]]:
                    window[s[l]] -= 1
                    newL = l + 1
                    while True:
                        if s[newL] not in tChars:
                            newL += 1
                            continue
                        else:
                            if window[s[newL]] > tChars[s[newL]]:
                                window[s[newL]] -= 1
                                newL += 1
                                continue
                            else:
                                l = newL
                                break
                if r - l + 1 < shortest[1]:
                    shortest = [s[l:r+1], r - l + 1]
        return shortest[0]
                

