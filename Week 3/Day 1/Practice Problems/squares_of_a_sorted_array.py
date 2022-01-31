class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Solution 1
        #l = []
        #for i in nums:
        #    l.append(i * i)
        #l.sort()
        #return l
        
        #Solution 2
        l = []
        posPointer = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                posPointer = i
                break
        if posPointer == 0:
            if nums[posPointer] >= 0:
                for i in range(len(nums)):
                    l.append(nums[i] * nums[i])
                return l
            else:
                for i in range(len(nums) - 1, -1, -1):
                    l.append(nums[i] * nums[i])
                return l
        negPointer = posPointer - 1
        while nums[negPointer] == 0 and negPointer >= 0:
            l.append(0)
            negPointer -= 1
        while negPointer >= 0 and posPointer < len(nums):
            if abs(nums[posPointer]) < abs(nums[negPointer]):
                l.append(nums[posPointer] * nums[posPointer])
                posPointer += 1
            else:
                l.append(nums[negPointer] * nums[negPointer])
                negPointer -= 1
        while posPointer < len(nums):
            l.append(nums[posPointer] * nums[posPointer])
            posPointer += 1
        while negPointer >= 0:
            l.append(nums[negPointer] * nums[negPointer])
            negPointer -= 1
        return l