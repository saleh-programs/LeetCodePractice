class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        minK = float("inf")
        maxK = float("-inf")
        for num in piles:
            maxK = max(maxK, num)

        l = 1
        r = maxK

        while l <= r:
            middle = l + int((r - l) / 2)

            hours = 0 
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / middle)
            if hours <= h:
                minK = min(minK, middle)
                r = middle - 1
            else:
                l = middle + 1

        return minK