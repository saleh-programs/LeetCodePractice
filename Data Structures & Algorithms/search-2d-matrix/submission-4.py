class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # trying optimal

        l, r = 0, len(matrix) * len(matrix[0])-1
        while (l <= r):
            middle = l + int((r-l) / 2)
            row, column = middle // len(matrix[0]), middle % len(matrix[0])
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False