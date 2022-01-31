def reverseArray(arr):
    #Solution 1
    #arr1 = sorted(arr, reverse = True)
    #return arr1
    
    #Solution 2
    #In-place reverse
    #Advantage: Space Optimal
    #Disadvantage: Original array is lost
    for i in range((len(arr) // 2)):
        temp = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 - i] = temp
    return arr

#Driver Code
q = int(input())
l = list(map(int, input().split())) #Get input array/ list
print(reverseArray(l))