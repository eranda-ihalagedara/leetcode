class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        offset = 2*numRows-2
        zz = ''
        for i in range(numRows):
            for j in range(0,n,offset):
                id1 = j+i
                if id1>=n:
                    continue
                zz+= s[id1]
                id2 = j+offset-i
                if id1<id2< j+offset and id2<n:
                    zz+= s[id2]
        
        return zz

    def convert_optimized(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows>=len(s):
            return s

        zz = ['']*numRows
        row, offset = 0, -1
        
        for c in s:
            zz[row] += c
            if row == 0 or row == numRows-1:
                offset *= -1
            row += offset
        
        return ''.join(zz)