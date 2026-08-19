class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        minK = maxK
        l = 1
        r = maxK-1
        while l <= r:
            middle = l + (r-l)//2
            hoursTaken = 0
            for pile in piles:
                hoursTaken += math.ceil(pile / middle)
            if hoursTaken <= h:
                minK = min(minK, middle)
                r = middle - 1
            else:
                l = middle + 1
        return minK

