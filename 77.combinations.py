class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[n]]
        arr = list(range(1,n+1))
        comb = []
        def build_combinations(pool, carr):
            if len(carr) == k:
                comb.append(carr)
                return

            for i in range(len(pool)):
                build_combinations(pool[i+1:], carr+[pool[i]])
        
        build_combinations(arr,[])

        return comb
		

    def combine_optimizedI(self, n: int, k: int) -> List[List[int]]:
        comb = []
        def build_combinations(num, carr):
            if len(carr) == k:
                comb.append(carr)
                return

            for i in range(num:n+1):
                build_combinations(i+1, carr+[i])
        
        build_combinations(arr,[])

        return comb