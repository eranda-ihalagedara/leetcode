class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1

        for i in range(len(digits)-1, -1, -1):
            add = carry
            carry = (digits[i]+add)//10
            digits[i] = (digits[i]+add)%10
			
			if carry ==0:
                return digits

        return [carry] + digits

    def plusOne_optimized(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            
            if digits[i]<9:
                digits[i]+=1
                return digits
                
            digits[i] = 0

        return [1] + [0]*len(digits)