class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        blocks = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in rows[i]:
                        return False
                    
                    rows[i].add(board[i][j])
                
                    if board[i][j] in cols[j]:
                        return False
                    cols[j].add(board[i][j])

                    bid = 3*(i//3) + j//3
                    if board[i][j] in blocks[bid]:
                        return False
                    blocks[bid].add(board[i][j])

        return True

    def isValidSudoku_optimized(self, board: List[List[str]]) -> bool:

        seen = set()

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if board[i][j]!=".":
                    if (0,i,board[i][j]) in seen:
                        return False
                    
                    seen.add((0,i,board[i][j]))
                
                    if board[i][j] in cols[j]:
                        return False
                    cols[j].add(board[i][j])

                    bid = 3*(i//3) + j//3
                    if board[i][j] in blocks[bid]:
                        return False
                    blocks[bid].add(board[i][j])

        return True
     