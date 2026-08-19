class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0 
        r = len(matrix[0]) * len(matrix) - 1
        while l <= r:
            middle = l + ((r-l) // 2)
            row = middle // len(matrix[0])
            col = middle % len(matrix[0])

            if matrix[row][col] < target:
                l = middle + 1
            elif matrix[row][col] > target:
                r = middle - 1
            else:
                return True
        return False
            