class MyQueue:
    # old old old old new 
    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        temp = []
        for i in range(len(self.st)):
            temp.append(self.st.pop())

        
        self.st.append(x)

        for i in range(len(temp)):
            self.st.append(temp.pop())

    def pop(self) -> int:
        return self.st.pop()

    def peek(self) -> int:
        return self.st[-1]

    def empty(self) -> bool:
        return not self.st


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()