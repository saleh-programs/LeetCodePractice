class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        t = 0
        b = len(matrix) - 1
        while t <= b:
            middleCol = t + ((b-t) // 2)

            if matrix[middleCol][0] > target:
                b = middleCol - 1
            elif matrix[middleCol][0] < target:
                t = middleCol + 1
            else:
                return True
        middleCol = b
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            middleRow = l + ((r - l) // 2)

            if matrix[middleCol][middleRow] > target:
                r = middleRow - 1
            elif matrix[middleCol][middleRow] < target:
                l = middleRow + 1
            else:
                return True
        return False