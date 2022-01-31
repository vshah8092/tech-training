class MyHashSet:

    def __init__(self):
        self.set = {}
        
    #The hash function used is bucketID = key % 10

    def add(self, key: int) -> None:
        val = key % 10
        if val in self.set.keys():
            if key not in self.set[val]:
                self.set[val].append(key)
        else:
            self.set[val] = [key]

    def remove(self, key: int) -> None:
        val = key % 10
        if val in self.set.keys():
            if key in self.set[val]:
                self.set[val].remove(key)

    def contains(self, key: int) -> bool:
        val = key % 10
        if val in self.set.keys():
            if key in self.set[val]:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)