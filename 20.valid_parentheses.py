class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        para = []

        for c in s:
            if c in '([{':
                para.append(c)
            else:
                if c in mapping:
                    if len(para)==0:
                        return False
                    
                    if mapping[c]!= para[-1]:
                        return False
                    para.pop()
        
        if len(para)>0:
                return False
        else:
            return True 