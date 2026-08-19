class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = float("-inf")
        for num in piles:
            maxPile = max(maxPile, num)
        
        l = 1
        r = maxPile
        while (l<=r):
            middle = l + (r-l) // 2

            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(pile / middle)
            
            if timeTaken <= h:
                k = middle
                r = middle - 1
            else:
                l = middle + 1
        return k