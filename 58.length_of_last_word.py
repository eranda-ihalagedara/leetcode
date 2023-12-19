class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rid = len(s)
        lid = rid - 1

        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                if s[lid] != ' ':
                    break
                rid = i
                lid = i
            else:
                lid = i
        
        return rid - lid
		

    def lengthOfLastWord_optimized(self, s: str) -> int:
        wlen = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                wlen += 1
            elif wlen >0:
                break
        
        return wlen