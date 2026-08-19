class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        preProduct = 1
        postProduct = 1
        for i in range(len(nums)):
            preProduct *= nums[i]
            postProduct *= nums[len(nums) - 1 - i]
            prefix.append(preProduct)
            postfix.insert(0, postProduct)
        prefix.append(1)
        postfix.append(1)
        result = []
        for i in range(len(nums)):
            result.append(prefix[i-1] * postfix[i+1])
        return result