# class Solution:
#     def trap(self, height: List[int]) -> int:
#         # first solution, not looking at recommended complexities TAKE 2
#         l = 0
#         r = len(height) - 1
#         leftMax = [0, -1]
#         rightMax = [0, -1]
#         totalWater = 0
#         while (l <= r):
#             if height[l] >= leftMax[0]:
#                 leftMax = [height[l], l]
#             if height[r] >= rightMax[0]:
#                 rightMax = [height[r], r]
#             if l == r:
#                 higherMax = [0, -1]
#                 if leftMax[0] > rightMax[0]:
#                     higherMax = leftMax
#                     lowerMax = rightMax
#                 else:
#                     higherMax = rightMax
#                     lowerMax = leftMax

#                 numinvalidAreas = (higherMax[0] - lowerMax[0]) * abs(higherMax[1] - l)
#                 print(higherMax[1], l, totalWater, numinvalidAreas)
#                 totalWater -= numinvalidAreas
#                 totalWater += (lowerMax[0] - height[l])
#                 break

#             if height[l] <= leftMax[0]:
#                 totalWater += (leftMax[0] - height[l])
#                 l += 1
#             elif height[r] <= rightMax[0]:
#                 totalWater += (rightMax[0] - height[r])
#                 r -= 1

#         return totalWater

class Solution:
    def trap(self, height: List[int]) -> int:
        # first solution, not looking at recommended complexities TAKE 3 (man i hope no one sees this)
        l = 0
        r = len(height) - 1
        leftMax = [0, -1]
        rightMax = [0, -1]
        totalWater = 0
        while (l <= r):
            # ok...
            if height[l] >= leftMax[0]:
                leftMax = [height[l], l]
            if height[r] >= rightMax[0]:
                rightMax = [height[r], r]
            #ok...wait
            if l == r:
                higherMax = [0, -1]
                if leftMax[0] > rightMax[0]:
                    higherMax = leftMax
                    lowerMax = rightMax
                else:
                    higherMax = rightMax
                    lowerMax = leftMax

                numinvalidAreas = (higherMax[0] - lowerMax[0]) * abs(higherMax[1] - l)
                print(l)
                print(higherMax[1], l, totalWater, numinvalidAreas)
                totalWater -= numinvalidAreas
                totalWater += (lowerMax[0] - height[l])
                break

            # ok...
            if height[l] < leftMax[0]:
                totalWater += (leftMax[0] - height[l])
                l += 1
                continue
            elif height[r] < rightMax[0]:
                totalWater += (rightMax[0] - height[r])
                r -= 1
                continue
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1

        return totalWater