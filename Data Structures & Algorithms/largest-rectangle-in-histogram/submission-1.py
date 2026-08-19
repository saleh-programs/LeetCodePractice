class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        maxArea = float('-inf')
        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i])
            if not stack:
                stack.append((heights[i], i))
                continue
            if stack[-1][0] == heights[i]:
                last = stack.pop()
                stack.append((heights[i], last[1]))
                maxArea = max(maxArea, stack[-1][0] * (i - stack[-1][1] + 1))
            if stack[-1][0] < heights[i]:
                stack.append((heights[i], i))
                maxArea = max(maxArea, stack[-2][0] * (i - stack[-2][1] + 1))
            else:
                maxArea = max(maxArea, heights[i] * (i - stack[-1][1] + 1))
                last = stack.pop()
                while stack and stack[-1][0] >= heights[i]:
                    last = stack.pop()
                stack.append((heights[i], last[1]))

        while stack:
            maxArea = max(maxArea, stack[-1][0] * (len(heights)-1 - stack[-1][1] + 1))
            stack.pop()
        return maxArea
