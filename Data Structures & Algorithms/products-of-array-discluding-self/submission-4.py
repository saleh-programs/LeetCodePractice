class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # my better (one pass) solution
        result = [1] * len(nums)
        prefixAcc = 1
        suffixAcc = 1

        for i in range(len(nums)):
            prefixAcc *= nums[i-1] if i != 0 else 1
            suffixAcc *= nums[len(nums)-1 - i + 1] if i != 0 else 1

            result[i] *= prefixAcc 
            result[len(nums)-1-i] *= suffixAcc
        return result