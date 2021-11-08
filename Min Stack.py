class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []
        

    def push(self, val: int) -> None:
        if len(self.min) == 0:
            self.min.append(val)
        elif val <= self.min[len(self.min)-1]:
            self.min.append(val)
        self.arr.append(val)
        

    def pop(self) -> None:
        if len(self.arr)==0:
            return None
        mimi = self.arr.pop()
        if mimi == self.min[len(self.min)-1]:
            self.min.pop()
        return mimi

    def top(self) -> int:
        if(len(self.arr)>0):
            return self.arr[len(self.arr)-1]
        

    def getMin(self) -> int:
        return self.min[len(self.min)-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()