class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while (l < r):
            while numbers[l] + numbers[r] > target and l < r:
                r -= 1
            while numbers[l] + numbers[r] < target and l < r:
                l += 1
            if l >= r:
                break
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
        return []
                