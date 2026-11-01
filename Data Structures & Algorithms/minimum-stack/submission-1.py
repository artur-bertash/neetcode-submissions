class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []

    def push(self, val: int) -> None:
        self.minSt.append(min(self.minSt[-1], val) if self.minSt else val)
        self.st.append(val)

    def pop(self) -> None:
        self.minSt.pop()
        self.st.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1]

    def getMin(self) -> int:
        return self.minSt[-1]
