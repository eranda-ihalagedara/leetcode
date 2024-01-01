class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s2t, t2s = {}, {}

        for i in range(len(s)):
            if s[i] not in s2t and t[i] not in t2s:
                s2t[s[i]] = t[i]
                t2s[t[i]] = s[i]
            elif s2t.get(s[i]) != t[i] or t2s.get(t[i]) != s[i]:
                    return False
            
        return True
