class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        operators = {'+', '-', '*', '/'}
        for t in tokens:
            if t in operators:
                b = operand_stack.pop()
                a = operand_stack.pop()
                if t == '+':
                    operand_stack.append(a+b)
                elif t=='-':
                    operand_stack.append(a-b)
                elif t=='*':
                    operand_stack.append(a*b)
                elif t=='/':
                    operand_stack.append(int(a/b))

            else:
                operand_stack.append(int(t))
        
        return operand_stack[-1]