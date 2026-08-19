from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = defaultdict(int)
        freqBucketList = [[] for _ in range(len(nums))]
        topK = []
        for num in nums:
            freqDict[num] += 1
        for num, freq in freqDict.items():
            freqBucketList[freq-1].append(num)
        print(freqBucketList)

        for i in range(len(freqBucketList)-1,-1,-1):
            for num in freqBucketList[i]:
                if (len(topK) == k):
                    return topK
                topK.append(num)

        return topK
