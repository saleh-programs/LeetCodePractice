class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # this shouldn't work
        res = []    
        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            if nums[i] > 0: 
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            while (l < r):
                total = nums[l] + nums[i] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[l],nums[i], nums[r]])
                    l += 1
                    r -= 1
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
        return res