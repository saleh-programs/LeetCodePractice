class Solution:
    def solve(self, board: List[List[str]]) -> None:
        outofbounds = lambda x: x[0] < 0 or x[1] < 0 or x[0] >= len(board) or x[1] >= len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        curr = [0,0]
        safe = set()

        def collect0s(i,j):
            queue = deque([(i,j)])
            safe.add(f"{i}-{j}")
            while queue:
                r,c = queue.popleft()
                neighbors = [(r+1,c),(r,c-1),(r-1,c),(r,c+1)]

                for nbr in neighbors:
                    if outofbounds(nbr):
                        continue
                    if board[nbr[0]][nbr[1]] == "O" and f"{nbr[0]}-{nbr[1]}" not in safe:
                        queue.append(nbr)
                        safe.add(f"{nbr[0]}-{nbr[1]}")
                

        
        turn = 0
        while turn < 4:
            if board[curr[0]][curr[1]] == "O" and f"{curr[0]}-{curr[1]}" not in safe:
                collect0s(curr[0],curr[1])

            nextVal = [curr[0] + directions[turn][0], curr[1] + directions[turn][1]]
            while outofbounds(nextVal):
                turn += 1
                if turn > 3:
                    break
                nextVal = [curr[0] + directions[turn][0], curr[1] + directions[turn][1]]
            curr = nextVal


        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and f"{i}-{j}" not in safe:
                    board[i][j] = "X"

            

