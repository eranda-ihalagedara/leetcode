class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        sdict,tdict = {},{}

        for i in range(len(s)):
            sdict[s[i]] = sdict.get(s[i],0)+1
            tdict[t[i]] = tdict.get(t[i],0)+1
        
        for key in sdict.keys():
            if sdict[key] != tdict.get(key,-1):
                return False
    
        return True
	
	
	def isAnagram_optimized(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        chardict = {}

        for i in range(len(s)):
            chardict[s[i]] = chardict.get(s[i],0)+1
            chardict[t[i]] = chardict.get(t[i],0)-1
        
        for key in chardict.keys():
            if chardict[key] != 0:
                return False
    
        return True