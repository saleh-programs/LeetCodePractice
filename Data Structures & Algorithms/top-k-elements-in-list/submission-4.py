class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDic = {}
        freqList = [[] for i in range(len(nums))]
        for num in nums:
            if num not in freqDic:
                freqDic[num] = 0
            freqDic[num] += 1
        for num, freq in freqDic.items():
            freqList[freq-1].append(num)
        result = []
        i = len(freqList)
        while len(result) < k:
            i -= 1
            result += freqList[i]
        while len(result) > k:
            result.pop()
        return result

