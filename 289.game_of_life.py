class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        status_update = []

        for i in range(m):
            for j in range(n):
                nr = [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j+1),(i+1,j+1), (i+1,j), (i+1,j-1), (i,j-1)]
                ones = 0
                for r,c in nr:
                    if -1<r<m and -1<c<n:
                        ones += board[r][c]
                
                if board[i][j]==1:
                    if ones<2 or ones>3:
                        status_update.append((i,j,0))
                else:
                    if ones==3:
                        status_update.append((i,j,1))
        
        for i,j,v in status_update:
            board[i][j] = v