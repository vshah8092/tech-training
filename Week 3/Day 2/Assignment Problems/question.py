class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            self.stack.append((val, max(val, self.stack[-1][1])))
        return
        
    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
        return
        
    def getMax(self):
        if len(self.stack) != 0:
            return self.stack[-1][1]
        return

#Driver Code
q = int(input())
s = Stack()
for i in range(q):
    l = list(map(int, input().strip().split()))
    if len(l) == 2:
        s.push(l[1])
    elif l[0] == 2:
        s.pop()
    else:
        print(s.getMax())