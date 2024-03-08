class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        h = len(grid)
        w = len(grid[0])

        items = set((i,j) for i in range(h) for j in range(w))
        nislands = 0

        while items:
            i,j = items. pop()

            if grid[i][j] == '1':
                # print(i,j)
                island = set()
                next_cell = set([(i,j)])

                while next_cell:
                    k,l = next_cell.pop()
                    neighbours = [(k+1,l), (k-1,l), (k,l+1), (k,l-1)]

                    for u,v in neighbours:
                        if -1<u<h and -1<v<w:
                            if grid[u][v] == '1' and (u,v) not in island:
                                next_cell.add((u,v))

                    island.add((k,l))
                    if (k, l) in items:
                        items.remove((k, l))

                island.add((i,j))

                nislands += 1

        return nislands
		
		

    def numIslands_optimized(self, grid: List[List[str]]) -> int:
        
        self.h = len(grid)
        self.w = len(grid[0])

        nislands = 0

        for i in range(self.h):
            for j in range(self.w):
                if grid[i][j] == '1':
                    self.dfs(grid, i,j)
                    nislands += 1

        return nislands
    
    def dfs(self, grid, i, j):
        if -1 < i < self.h and -1 < j < self.w and grid[i][j] == '1':
            grid[i][j] = '0'

            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)