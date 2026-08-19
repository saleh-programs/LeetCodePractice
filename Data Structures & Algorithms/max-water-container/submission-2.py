class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # result = min(height1, height2) * (r - l)
        result = 0
        l = 0
        r = len(heights)-1
        while l < r:
            if heights[l] < heights[r]:
                result = max(result, heights[l] * (r-l)) 
                l += 1
            elif heights[l] > heights[r]:
                result = max(result, heights[r] * (r-l)) 
                r -= 1
            else:
                result = max(result, heights[l] * (r-l)) 
                l += 1
                r -= 1
        return result
            
            
