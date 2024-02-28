class MinStack:

    def __init__(self):
        self.stk = []
        self.stmin = 2**31
        self.minflag = True

    def push(self, val: int) -> None:
        self.stk.append(val)
        if val < self.stmin: self.stmin = val

    def pop(self) -> None:
        val = self.stk.pop()
        if val == self.stmin:
            self.minflag = False
        return val

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        if self.minflag:
            return self.stmin
        stmin = 2**31

        for v in self.stk:
            if v < stmin: stmin = v

        return stmin


class MinStack_optimized_I:

    def __init__(self):
        self.stk = []
        self.stmin = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        
        if self.stmin:
            self.stmin.append(min(val,self.stmin[-1]))
        else:
            self.stmin.append(val)
        

    def pop(self) -> None:
        self.stk.pop()
        self.stmin.pop()

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.stmin[-1]
		

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()