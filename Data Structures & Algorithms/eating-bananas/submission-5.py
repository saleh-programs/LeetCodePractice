class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        k = -9999
        for size in piles:
            k = max(size, k)

        l = 1
        r = k
        while l <= r:
            middle =  l + ((r - l) // 2)
            numHours = 0
            for size in piles:
                numHours += math.ceil(size / middle)
            if numHours > h:
                l = middle + 1
            elif numHours <= h:
                r = middle - 1

        return l