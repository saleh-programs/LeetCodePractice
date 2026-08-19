class Solution:

    def encode(self, strs: List[str]) -> str:
        len_list = [str(len(word)) for word in strs]
        return f"{'-'.join(len_list)}:{''.join(strs)}"
    def decode(self, s: str) -> List[str]:
        if len(s) == 1:
            return []
        separator_idx = s.find(":")
        lengths = s[:separator_idx].split("-")
        content = s[separator_idx+1:]
        
        result = []
        current_idx = 0
        for num in lengths:
            length = int(num)
            result.append(content[current_idx:current_idx + length])
            current_idx += length
        return result