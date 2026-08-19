class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = []
        visited = set()
        
        def dfs(i):
            stack.append(nums[i])
            visited.add(nums[i])

            if len(visited) == len(nums):
                result.append(stack.copy())

            for j in range(len(nums)):
                if nums[j] not in visited:
                    dfs(j)

            stack.pop()
            visited.remove(nums[i])
            

        for i in range(len(nums)):
            dfs(i)
        return result

            
