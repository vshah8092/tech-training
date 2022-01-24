class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None for i in range(k)]
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.front == -1:
                self.front = 0
                self.rear = 0
                self.queue[self.front] = value
            else:
                self.rear = (self.rear + 1) % self.size
                self.queue[self.rear] = value
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return True
        else:
            return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.front == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.rear + 1) % self.size == self.front:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()