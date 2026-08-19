class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        monDecStack = []
        result = []

        for i in range(len(temperatures) - 1, -1, -1):
            while len(monDecStack):
                if temperatures[i] >= monDecStack[-1][0]:
                    monDecStack.pop()
                else:
                    result.append(monDecStack[-1][1] - i)
                    monDecStack.append([temperatures[i], i])
                    break
            if not len(monDecStack):
                monDecStack.append([temperatures[i], i])
                result.append(0)
        return result[::-1]

            


            

