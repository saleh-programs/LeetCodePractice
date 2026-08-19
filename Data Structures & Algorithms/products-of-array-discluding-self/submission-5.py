class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the obvious solution
        result = []
        product = 1
        productWithoutZero = 1

        for i in range(len(nums)):
            if nums[i] != 0 or product == 0 :
                productWithoutZero *= nums[i]
            product *= nums[i]



        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(productWithoutZero)
            else:
                result.append(int(product / nums[i]))
        return result