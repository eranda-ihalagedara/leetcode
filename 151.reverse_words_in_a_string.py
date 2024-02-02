class Solution:
    def reverseWords(self, s: str) -> str:
        
        rstr = ''

        l = 0

        for i in range(len(s)):
            if s[i]==' ':
                if s[l]!=' ':
                    rstr = s[l:i] + ' ' + rstr

                l = i
            else: 
                if s[l]==' ':
                    l = i
        
        if s[l]!=' ' and s[-1]!=' ':
            rstr = s[l:] + ' ' + rstr

        return rstr[:-1]
