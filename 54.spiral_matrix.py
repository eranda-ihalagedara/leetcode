class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        h = len(matrix)
        w = len(matrix[0])
        spiral = []
        r,c = 0,0

        while w>0 or h>0:

            # Right
            if w>0:
                spiral += matrix[r][c:c+w]
                c = c+w-1
                w-=1
            else:
                break
          
            # Down
            if h>1:
                for i in range(1,h):
                    spiral.append(matrix[r+i][c])
                r = r+h-1
                h-=1
            else:
                break
            
            # Left
            if w>0:
                spiral += matrix[r][c-w:c][::-1]
                c = c-w
                w-=1
            else:
                break
            
            # Up
            if h>1:
                for i in range(1,h):
                    spiral.append(matrix[r-i][c])
                r = r-h+1
                c = c+1
                h-=1
            else:
                break

        return spiral


    def spiralOrder_optimized(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        top=0
        bottom=m-1
        left=0
        right=n-1
        l=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                l.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                l.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    l.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    l.append(matrix[i][left])
                left+=1
        return l