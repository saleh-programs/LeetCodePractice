from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        for i in range(len(board)):
            rowNums = set()
            columnNums = set()
            for j in range(len(board[i])):
                value = board[i][j]
                if value != ".":
                    # squares
                    if value in squares[f"{i // 3}{j // 3}"]:
                        return False
                    squares[f"{i // 3}{j // 3}"].add(value)

                    # row duplicates
                    if value in rowNums:
                        return False
                    rowNums.add(value)
                
                value2 = board[j][i]
                if value2 != ".":
                    # column duplicates
                    if value2 in columnNums:
                        return False
                    columnNums.add(value2)
        return True



