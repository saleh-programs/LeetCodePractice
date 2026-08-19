class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        backupProduct = 1
        for num in nums:
            if num != 0 or product == 0:
                backupProduct *= num
            product *= num

        return [product // num if num != 0 else backupProduct  for num in nums ]