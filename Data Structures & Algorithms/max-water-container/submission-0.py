class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # BAD SOLUTION
        maxWater = 0
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                area = (j - i) * min(heights[i],heights[j])
                maxWater = max(maxWater,area)
        return maxWater