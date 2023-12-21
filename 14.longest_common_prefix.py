class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        if len(strs) == 0 or strs[0] == "":
            return prefix

        for i in range(200):
            if i > len(strs[0])-1:
                return prefix
            c_char = strs[0][i]

            for j in range(1,len(strs)):
                if i > len(strs[j])-1 or strs[j][i] != c_char:
                    return prefix
            
            prefix += c_char
        
        return prefix


    def longestCommonPrefix_optimized1(self, strs: List[str]) -> str:
        
        prefix = ""
        i = 0
        while True:
            if i >= len(strs[0]):
                return prefix
            c_char = strs[0][i]
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != c_char:
                    return prefix
            prefix += c_char
            i+=1


    def longestCommonPrefix_optimized2(self, strs: List[str]) -> str:
        
        if len(strs) ==0:
            return ""
        prefix = strs[0]
 
        for i in range(len(prefix)):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != prefix[i]:
                    return prefix[:i]

        return prefix
		
		
    def longestCommonPrefix_optimized3(self, strs: List[str]) -> str:
        
        strs=sorted(strs)
        st0=strs[0]
        stn=strs[-1]
        prefix = ""
        lmin = min(len(st0),len(st0))
        for i in range(lmin):
            if(st0[i]!=stn[i]):
                return prefix
            prefix += st0[i]

        return prefix