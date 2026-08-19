class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = []
        visited = set()
        i = 0
        while i < len(nums) and nums[i] <= 0 :
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue

            
            target = -nums[i]

            l = i + 1
            r = len(nums) - 1
            while (l < r):
                if (nums[l] + nums[r] == target):
                    if f"{nums[i]},{nums[l]},{nums[r]}" not in visited:
                        triplets.append([nums[i], nums[l], nums[r]])
                        visited.add(f"{nums[i]},{nums[l]},{nums[r]}")
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else: 
                    l += 1
            i += 1
        return triplets
