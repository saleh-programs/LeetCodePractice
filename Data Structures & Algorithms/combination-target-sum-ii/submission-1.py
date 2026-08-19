class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        total = 0
        stack = []
        nums = candidates

        nums.sort()
        
        def dfs(index):
            nonlocal total

            total += nums[index]
            stack.append(nums[index])

            if total < target:
                for i in range(index+1,len(nums)):
                    if total + nums[i] <= target and (i==index+1 or nums[i]!= nums[i-1]):
                        dfs(i)
            elif total == target:
                result.append(stack.copy())

            total -= nums[index]
            stack.pop()
        print(nums)
        for i in range(0,len(nums)): 
            if nums[i] <= target and (i==0 or nums[i] != nums[i-1]):
                dfs(i)
        return result