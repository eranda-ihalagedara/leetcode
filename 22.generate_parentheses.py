class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        comb = []

        def backtrack(l,r, seq):

            if len(seq) == 2*n:
                comb.append(seq)
            
            if l < n:
                backtrack(l+1,r, seq+'(')
            
            if r < l:
                backtrack(l, r+1, seq+')')

        backtrack(0,0,'')
        return comb

    def generateParenthesis_iterative(self, n: int) -> List[str]:
        
        comb = []
        queue = [(0,0,'')]

        while queue:
            l, r, seq = queue.pop()

            if len(seq) == 2*n:
                comb.append(seq)
                continue
            
            if l < n:
                queue.append((l+1,r, seq+'('))
            if r < l:
                queue.append((l,r+1, seq+')'))

        return comb


    def generateParenthesis_optimized(self, n: int) -> List[str]:
        
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]