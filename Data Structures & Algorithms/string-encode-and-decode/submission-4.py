class Solution:

    def encode(self, strs: List[str]) -> str:
        wordLengths = [str(len(word)) for word in strs]
        initialStr = "-".join(wordLengths) + ':'
        result = initialStr + "".join(strs)
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        separator = s.find(':')
        if separator == 0:
            return []
            
        wordLengths = (s[0:separator]).split("-")
        result = []

        currInd = separator + 1
        for strLength in wordLengths:
            length = int(strLength)
            result.append(s[currInd:currInd+length])
            currInd = currInd + length
        return result