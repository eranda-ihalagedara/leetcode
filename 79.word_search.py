class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        wl = len(word)

        visited = [[0]*n for _ in range(m)]

        def dfs(idx, i, j, visited):
            
            if idx ==  wl: return True

            nr = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
            
            for k, l in nr:
                if (0 <= k < m) and (0 <= l < n) and not visited[k][l]:
                    if board[k][l] == word[idx]:
                        visited[k][l] = 1
                        if dfs(idx+1, k, l, visited): return True
                        visited[k][l] = 0
            return False
		
		
		# Reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
			
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    visited[i][j] = 1
                    if dfs(1, i, j, visited):
                        return True
                    visited[i][j] = 0
        return False