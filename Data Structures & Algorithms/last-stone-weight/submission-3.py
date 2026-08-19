class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # attempt at bucket sort method
        maxStone = max(stones)
        weights = [0] * (maxStone+1)
        for s in stones:
            weights[s] += 1

        current = maxStone
        stone1 = 0
        print(weights)
        while current > 0:
            if stone1 and weights[current]:
                weights[current] -= 1
                if stone1 - current >= current:
                    stone1 = stone1 - current
                else:
                    weights[stone1 - current] += 1
                    stone1 = 0
                continue
            if weights[current] >= 1 and weights[current] % 2 != 0:
                stone1 = current
            current -= 1
        return stone1
            








            
