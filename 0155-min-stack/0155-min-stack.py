class MinStack:

    def __init__(self):
        self.arr = []
        self.min_arr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.min_arr: 
            if val < self.min_arr[-1]: 
                self.min_arr.append(val)
            else: 
                self.min_arr.append(self.min_arr[-1])
        else: 
            self.min_arr.append(val)
        

    def pop(self) -> None:
        self.arr.pop()
        self.min_arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min_arr[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()