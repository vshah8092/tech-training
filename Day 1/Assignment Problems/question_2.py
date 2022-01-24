class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_node(self, data = None):
        n = Node(data = data)
        end = self.head
        while end.next != None:
            end = end.next
        end.next = n

def printLinkedList(head):
    while head != None:
        print(head.data)
        head = head.next

#Driver Code
p = int(input())
l = LinkedList()
for i in range(p):
    if i == 0:
        l.head = Node(int(input()))
    else:
        l.add_node(int(input()))
printLinkedList(l.head)