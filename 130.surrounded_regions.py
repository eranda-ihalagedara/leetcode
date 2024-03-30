class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[0]*n for _ in range(m)]

        self.island_list = []

        def explore_island(i,j, board):

            island = []
            queue = [(i,j)]
            attatched_to_edge = False

            while queue:
                x, y = queue.pop()
                if not (0<x<m-1 and 0<y<n-1):
                    attatched_to_edge = True
                nr = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

                for k,l in nr:
                    if 0<=k<m and 0<=l<n:
                        if board[k][l] == 'O' and not visited[k][l]:
                            queue.append((k,l))

                island.append((x,y))
                visited[x][y] = 1
            
            if not attatched_to_edge:
                self.island_list += island


        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    explore_island(i,j, board)
        
        for i,j in self.island_list:
            board[i][j] = 'X'


    def solve_optimizedI(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def explore_island(i,j):
            
            if i<0 or j<0 or i==m or j == n or board[i][j] != 'O': return
            
            board[i][j] = 'Y'

            explore_island(i-1, j)
            explore_island(i+1, j)
            explore_island(i, j-1)
            explore_island(i, j+1)


        for i in range(m):
            if board[i][0] == 'O':
                explore_island(i,0)
            if board[i][n-1] == 'O':
                explore_island(i,n-1)
        for j in range(1,n-1):
            if board[0][j] == 'O':
                explore_island(0,j)
            if board[m-1][j] == 'O':
                explore_island(m-1,j)
            

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'