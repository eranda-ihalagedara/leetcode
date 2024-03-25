class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        l = len(candidates)
        combinations = []
        multiples = [0]*l
        mul_lim = [target//x for x in candidates]
        
        def dfs(idx, csum, multiples):
            if idx == l or csum > target:
                return
            if csum == target:
                comb = []
                for i in range(l):
                    for j in range(multiples[i]):
                        comb.append(candidates[i])
                combinations.append(comb)
                return

            mul_idx = multiples[idx]
            for p in range(mul_lim[idx]+1):
                csum += candidates[idx]*p
                multiples[idx] = p
                dfs(idx+1, csum, multiples)
                csum -= candidates[idx]*p
            multiples[idx] = mul_idx
        dfs(-1, 0, multiples)

        return combinations
                
				
    def combinationSum_optimizedI(self, candidates: List[int], target: int) -> List[List[int]]:

        l = len(candidates)
        combinations = []

        def dfs(idx, csum, comb):
            if csum == target:
                combinations.append(comb.copy())
                return
            if csum > target:
                return

            for i in range(idx, l):
                comb.append(candidates[i])
                dfs(i, csum+candidates[i], comb)
                comb.pop()
            
        dfs(0, 0, [])

        return combinations
		

	# Dynamic Programming
    def combinationSum_optimizedI(self, candidates: List[int], target: int) -> List[List[int]]:

        dp = [[] for _ in range(target + 1)]
        for c in candidates:
            if c > target:
                continue
            dp[c].append([c])
            for i in range(c + 1, target+1):
                for comb in dp[i-c]:
                    dp[i].append(comb + [c])
        return dp[target]