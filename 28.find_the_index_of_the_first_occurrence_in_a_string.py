class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ln = len(needle)
        for i in range(len(haystack)-ln+1):
            if haystack[i:i+ln] == needle:
                return i
        return -1
	
	
	def strStr_optimized1(self, haystack: str, needle: str) -> int:
        ln = len(needle)
        lh = len(haystack)
        i, j = 0, 0

        while i < lh and j < ln:
            if haystack[i] == needle[j]:
                j += 1
            else:
                i -= j
                j = 0
            i += 1
        if j == ln:
            return i - ln
        else:
            return -1
	
	
	def strStr_optimized2(self, haystack: str, needle: str) -> int:
        ln = len(needle)
        lh = len(haystack)

        lps = self.build_lps(needle, ln)
        j = 0
        for i in range(lh):
            while haystack[i] != needle[j] and j > 0:
                j = lps[j-1]
            if haystack[i] == needle[j]:
                j += 1
                if j == ln:  # found a fully matching!
                    return i - ln + 1
        return -1

    def build_lps(self, needle, ln):
        lps = [0] * ln
        j = 0
        for i in range(1, ln):
            while needle[i] != needle[j] and j > 0:
                j = lps[j-1]
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j
        return lps