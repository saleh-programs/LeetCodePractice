class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None
    def push(self, val: int) -> None:
        if self.minVal is None:
            self.minVal = val
        else:
            self.minVal = min(self.minVal, val)
        self.stack.append((val, self.minVal))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minVal = self.stack[-1][1]
        else:
            self.minVal = None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None