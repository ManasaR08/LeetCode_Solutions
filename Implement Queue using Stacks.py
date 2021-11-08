class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        while(len(self.s1) > 1):
            val = self.s1.pop()
            self.s2.append(val)
        out = self.s1.pop()
        for i in range(len(self.s2)):
            val = self.s2.pop()
            self.s1.append(val)
        return out
        

    def peek(self) -> int:
        return self.s1[0]        

    def empty(self) -> bool:
        if len(self.s1)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()