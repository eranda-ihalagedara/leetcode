from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}

        for i in range(len(magazine)):
            mag_dict[magazine[i]] = mag_dict.get(magazine[i],0) + 1
        

        for i in range(len(ransomNote)):
            if mag_dict.get(ransomNote[i],0) == 0:
                return False
                
            
            mag_dict[ransomNote[i]] -= 1

        return True
		
	
	def canConstruct_alternative(self, ransomNote: str, magazine: str) -> bool:
        ran, mag = Counter(ransomNote), Counter(magazine)

        return ran & mag == ran