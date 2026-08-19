class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        newPos = [(position[i], speed[i]) for i in range(n)]
        newPos = sorted(newPos,key=lambda x: x[0])

        fleets = 0
        maxHours = float("-inf")
        while newPos:
            car = newPos.pop()

            hours = (target - car[0]) / car[1]
            if hours > maxHours:
                fleets += 1
                maxHours = hours
        return fleets