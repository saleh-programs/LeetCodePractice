class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decStack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not decStack or temperatures[i] <= decStack[-1][0]:
                decStack.append((temperatures[i], i))
            else:
                while len(decStack) >= 1 and temperatures[i] > decStack[-1][0]:
                    temp, index = decStack.pop()
                    result[index] = i - index
                decStack.append((temperatures[i], i))
        return result

