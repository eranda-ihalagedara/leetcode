class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        ans = ''
        la, lb = len(a), len(b)
        if la<lb:
            a,b = b,a
            la,lb = lb, la

        carry = 0

        for i in range(la-1,-1,-1):
            if i-la+lb<0:
                ans = str((int(a[i])+carry)%2) + ans
                carry = (int(a[i])+carry)//2
            else:
                ans = str((int(a[i])+int(b[i-la+lb])+carry)%2) + ans
                carry = (int(a[i])+int(b[i-la+lb])+carry)//2

        if carry ==1:
            return '1'+ans
        return ans


    def addBinary_optimized(self, a: str, b: str) -> str:
        
        ans = ''
        i, j = len(a)-1, len(b)-1
        carry = 0
        ord0 = ord('0')

        while i>=0 or j>=0:
            csum  = carry
            if i>=0: csum += ord(a[i])-ord0
            if j>=0: csum += ord(b[j])-ord0
            ans = str(csum%2) + ans
            carry = csum//2
            i-=1
            j-=1

        if carry:
            return '1'+ans
        return ans
