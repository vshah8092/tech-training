class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue2.append(x)
        while len(self.queue1) != 0:
            self.queue2.append(self.queue1[0])
            self.queue1 = self.queue1[1:]
        self.temp = self.queue1
        self.queue1 = self.queue2
        self.queue2 = self.temp

    def pop(self) -> int:
        if not self.empty():
            a = self.queue1[0]
            self.queue1 = self.queue1[1:]
            return a

    def top(self) -> int:
        if not self.empty():
            return self.queue1[0]

    def empty(self) -> bool:
        if len(self.queue1) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()