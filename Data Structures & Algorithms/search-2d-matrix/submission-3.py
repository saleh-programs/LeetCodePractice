class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # STOP MARKING IT WRONG
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        if n + 1 == 0:
            return False

        t = 0
        b = m
        row = -1
        while (t <= b):
            middle = t + int((b-t) / 2)
            if matrix[middle][0] <= target and matrix[middle][n] >= target:
                row = middle
                break
            elif matrix[middle][n] < target:
                t = middle + 1
            else:
                b = middle - 1
        if row == -1:
            return False

        l = 0
        r = n

        while (l <= r):
            middle = l + int((r-l) / 2)

            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False