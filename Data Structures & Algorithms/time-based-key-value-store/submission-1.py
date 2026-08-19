class TimeMap:

    def __init__(self):
        self.valueMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.valueMap:
            self.valueMap[key] = [1,(timestamp, value)]
        else:
            self.valueMap[key].append((timestamp, value))
            self.valueMap[key][0] += 1
    def get(self, key: str, timestamp: int) -> str:
        if key in self.valueMap:
            l = 1
            r = len(self.valueMap[key]) - 1
            while l <= r:
                middle = l + ((r-l) // 2)
                currTimestamp, currValue = self.valueMap[key][middle]
                if currTimestamp ==  timestamp:
                    return currValue
                elif currTimestamp < timestamp:
                    l = middle + 1
                else:
                    r = middle - 1
            if r > 0:
                return self.valueMap[key][r][1]
        return ""
        
