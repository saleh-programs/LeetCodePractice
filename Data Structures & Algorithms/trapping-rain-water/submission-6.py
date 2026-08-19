class Solution:
    def trap(self, height: List[int]) -> int:
        

        stack = []
        total = 0

        for i in range(len(height)):
            if len(stack) and height[i] >= stack[-1][0]:
                lowest = stack[-1]
                while len(stack) and height[i] >= stack[-1][0]:
                    total += (min(stack[-1][0], height[i]) - lowest[0]) * ((i - 1) - stack[-1][1])
                    lowest = stack.pop()
                if len(stack):
                    total += (min(stack[-1][0], height[i]) - lowest[0]) * ((i - 1) - stack[-1][1])

            stack.append([height[i],i])
        return total

        
            
                    
            