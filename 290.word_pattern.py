class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words)!= len(pattern):
            return False
            
        s2p, p2s = {},{}
        for i in range(len(pattern)):
            if words[i] not in s2p and pattern[i] not in p2s:
                   s2p[words[i]]  =  pattern[i]
                   p2s[pattern[i]]  =  words[i]
            elif s2p.get(words[i])!= pattern[i] or p2s.get(pattern[i])!= words[i]:
                return False

        return True