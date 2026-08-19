class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {')':'(', '}':'{', ']':'['}
        for ch in s:
            if ch not in closing:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != closing[ch]:
                    return False
                stack.pop()
        return len(stack) == 0 