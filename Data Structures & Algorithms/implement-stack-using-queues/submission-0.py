class MyStack:
    # que = [1, 2, 3, 4]
    def __init__(self):
        self.q = deque()


    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        temp = deque()
        while len(self.q) > 1:
            temp.append(self.q.popleft())
        res = self.q.popleft()

        while temp:
            self.q.append(temp.popleft())
        
        return res
    def top(self) -> int:
        temp = deque()
        while len(self.q) > 1:
            temp.append(self.q.popleft())
        res = self.q[0]        
        temp.append(self.q.popleft())
        
        while temp:
            self.q.append(temp.popleft())
        return res

    def empty(self) -> bool:
        return not len(self.q)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()