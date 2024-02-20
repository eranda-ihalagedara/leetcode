class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = []

        while len(strs)>1:
            wrd = strs.pop()
            group.append([wrd])
            i=0
            while i <len(strs):
                if i>=len(strs):
                    break
                if len(wrd)== len(strs[i]):
                    flag = True
                    for c in strs[i]:
                        if c not in wrd:
                            flag=False
                            break
                    if flag:
                        group[-1].append(strs.pop(i))
                    else:
                        i+=1
                else:
                    i+=1
        if strs:
            group.append(strs)
        
        return group
    

    def groupAnagrams_optimizedI(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            wkey = ''.join(sorted(s))
            if wkey in group:
                group[wkey].append(s)
            else:
                group[wkey]=[s]
        
        return group.values()