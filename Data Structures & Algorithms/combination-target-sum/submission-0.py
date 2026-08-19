class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        total = 0
        stack = []
        def dfs(index):
            nonlocal total
            stack.append(nums[index])
            total += nums[index]

            if total < target:
                for i in range(index, len(nums)):
                    if total + nums[i] <= target:
                        dfs(i)
            else:
                result.append(stack.copy())
            stack.pop()
            total -= nums[index]
        for i in range(len(nums)):
            dfs(i)
        return result

