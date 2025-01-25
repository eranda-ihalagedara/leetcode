from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        output = []
        eq_map = defaultdict(dict)

        for [n,d], val in zip(equations, values):
            eq_map[n][d] = val
            eq_map[d][n] = 1/val

        def search_ratio(a, b, seq):

            sub_map = eq_map[a]
            if not sub_map: return -1.0
            if b in sub_map: return sub_map[b]

            for key in sub_map:
                if key in seq:  continue
                
                seq.append(key)
                r = search_ratio(key, b, seq)
                if r>0: return sub_map[key]*r
                seq.pop()
                
            return -1.0
        
        return [search_ratio(a, b, [a]) for a, b in queries]