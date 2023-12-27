class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal_flag = True
        s = s.lower()
        lid, rid = 0, len(s)-1
        
        while lid < rid:
            if (97<= ord(s[lid]) <=122 ) or (48<= ord(s[lid]) <=57 ):
                if (97<= ord(s[rid])<=122) or (48<= ord(s[rid]) <=57):
                    if s[lid] != s[rid]:
                        pal_flag = False
                        break
                    else:
                        lid += 1
                        rid -= 1
                else:
                    rid -= 1
            else:
                lid += 1

        return pal_flag
		
    def isPalindrome_optimized(self, s: str) -> bool:
        pal_flag = True
        s = ''.join(c for c in s if c.isalnum()).lower()
        l = len(s)-1
        i = 0

        while i < l-i:
            if s[i] != s[l-i]:
                pal_flag = False
                break
            i+=1

        return pal_flag
		


    def isPalindrome_optimized2(self, s: str) -> bool:
        pal_flag = True
        s = s.lower()
        lid, rid = 0, len(s)-1
        
        while lid < rid:
            if s[lid].isalnum():
                if s[rid].isalnum():
                    if s[lid] != s[rid]:
                        pal_flag = False
                        break
                    else:
                        lid += 1
                        rid -= 1
                else:
                    rid -= 1
            else:
                lid += 1

        return pal_flag