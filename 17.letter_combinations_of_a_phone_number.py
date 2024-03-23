class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        char_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        perm = []
        l = len(digits)
        idx = [[0,len(char_map[x])] for x in digits]
        
        def has_next(idx):
            for i, l in idx:
                if i != l-1: return True
            return False

        def next_id(idx):
            carry = 1
            for j in range(l):
                v = (idx[j][0]+carry) % idx[j][1]
                carry = (idx[j][0]+carry) // idx[j][1]
                idx[j][0] = v
                if carry == 0:
                    break

        while has_next(idx):
            p = ''
            for k in range(l):
                p += char_map[digits[k]][idx[k][0]]
            perm.append(p)
            next_id(idx)
        
        p = ''
        for k in range(l):
            p += char_map[digits[k]][-1]
        perm.append(p)

        return perm
		
		
    def letterCombinations_optimized(self, digits: str) -> List[str]:
        if digits == '':
            return []

        char_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        perm = []
        l = len(digits)

        def build_permutations(idx, cword):
            if idx == l:
                perm.append(cword)
                return

            for c in char_map[digits[idx]]:
                build_permutations(idx+1, cword+c)

        build_permutations(0, '')