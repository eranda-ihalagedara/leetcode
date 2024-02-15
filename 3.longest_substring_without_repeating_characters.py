class Solution:
    def lengthOfLongestSubstring_optimized(self, s: str) -> int:
        
        n = len(s)
        if n==0:
            return 0

        charindex = {}

        sublen = 0
        left = 0

        for right in range(n):
            
            if s[right] in charindex: 
                
                left = max(left, charindex[s[right]] + 1)

                if sublen >= n-left: 
                    break

            charindex[s[right]] = right
            sublen = max(sublen,right - left+1)

        return sublen
	