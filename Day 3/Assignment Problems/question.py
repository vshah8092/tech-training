#Importing required libraries
import math
import heapq

#Modified function for heappush
def push(heap, l):
    a = l.pop()[::-1] #[::-1] is used to Reverse
    heapq.heappush(heap, a)
    
    return heap, l

def avgWaitTime(l, n):
    #To find minimum average waiting time,
    #we use Shortest Job First (SJF) scheduling algorithm.
    #Since we cannot interrupt a job in between,
    #it is non-preemptive scheduling.
    answer = 0
    heap = [] #Use Heap data structure
    t = 0 #Keep track of time elapsed
    
    l.sort(reverse = True)

    while len(l) != 0 or len(heap) != 0:
        while len(l) != 0 and l[-1][0] <= t:
            heap, l = push(heap, l)
            
        if len(heap) != 0:
            a = heapq.heappop(heap)
            t += a[0]
            answer += (t - a[1])
        else:
            heap, l = push(heap, l)
            t = heap[0][1]

    answer = answer / n
    return math.floor(answer)

#Driver Code
n = int(input())
l = []

for i in range(n):
    l1 = list(map(int, input().split()))
    l.append((l1[0], l1[1]))

print(avgWaitTime(l, n))
