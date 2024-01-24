class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s:
            return 0
        
        decodings = [0]*(len(s)+1)

        decodings[0] = 1
        decodings[1] = 0 if s[0]=="0" else 1

        for i in range(2,len(s)+1):
            if 0< int(s[i-1])<10:
                decodings[i]+=decodings[i-1]
            if 10<= int(s[i-2:i]) <= 26:
                decodings[i]+=decodings[i-2]
        
        return decodings[-1]
	

    def numDecodings_optimized(self, s: str) -> int:
        
        if not s:
            return 0
        
        n1 = 1
        n2 = 0 if s[0]=="0" else 1

        for i in range(2,len(s)+1):
            ni = n2 if 0< int(s[i-1])<10 else 0
            if 10<= int(s[i-2:i]) <= 26:
                ni+=n1
            n1, n2 = n2, ni
        
        return n2