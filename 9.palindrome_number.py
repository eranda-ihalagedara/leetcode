class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_st = str(x)
        l,r = 0, len(x_st)-1

        while l<r:
            if x_st[l] != x_st[r]:
                return False
            l+=1
            r-=1
        return True

    def isPalindrome_II(self, x: int) -> bool:

        if x<0 or (x>0 and x%10==0):
            return False

        rev = 0

        while x>rev:
            rev = rev*10 + x%10
            x //=10
            
        return x==rev or x==rev//10