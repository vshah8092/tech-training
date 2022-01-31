class Solution:
    def sumSq(self, n):
        sum = 0
        while n > 0:
            sum += (n % 10) * (n % 10)
            n = n // 10
        return sum
        
    def isHappy(self, n: int) -> bool:
        s = set()
        a = 0
        b = 1
        while a + 1 == b:
            a = len(s)
            n = self.sumSq(n)
            if n == 1:
                return True
            s.add(n)
            b = len(s)
        return False