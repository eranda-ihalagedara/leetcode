class Solution:
    def intToRoman(self, num: int) -> str:
        vmap = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        values = [1,5,10,50,100, 500, 1000]
        roman = ''
        tens = 1
        while num >0:
            idx = tens*2
            v = num%10
            num = num//10
            if v == 9:
                roman = vmap[values[idx-2]] + vmap[values[idx]]+ roman
            elif v>=5:
                roman = vmap[values[idx-1]] + vmap[values[idx-2]]*(v%5) + roman
            elif v == 4:
                roman = vmap[values[idx-2]] + vmap[values[idx-1]] + roman
            else:
                roman = vmap[values[idx-2]]*v + roman
            tens+=1
        
        return roman
		
    def intToRoman_optimized(self, num: int) -> str:
        vmap = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        roman = ''
        
        for v in vmap.keys():
            while num >= v:
                roman+= vmap[v]
                num -= v
        
        return roman