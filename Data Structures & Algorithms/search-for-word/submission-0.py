class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        idx = 0
        visited = set()

        def detectWord(i, j):
            nonlocal idx
            idx += 1
            visited.add(f"{i}-{j}")
            if len(word) == idx:
                return True 

            neighbors = [[i,j-1],[i+1,j],[i,j+1],[i-1,j]]

            for each in neighbors:
                if each[0] < 0 or each[1] < 0 or each[0] >= len(board) or each[1] >= len(board[0]):
                    continue
                elif f"{each[0]}-{each[1]}" in visited:
                    continue
                elif board[each[0]][each[1]] == word[idx] and detectWord(each[0], each[1]):
                    return True
            idx -= 1
            visited.remove(f"{i}-{j}")
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and detectWord(i,j):
                    return True
        return False

                
        

