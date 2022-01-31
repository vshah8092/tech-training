class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #Solution 1
        #arr = sorted(set(nums))
        #if len(arr) < 3:
        #    return arr[-1]
        #else:
        #    return arr[-3]
        
        #Solution 2
        max1 = -2**31 - 1
        max2 = -2**31 - 1
        max3 = -2**31 - 1
        for i in nums:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2 and max1 != i:
                max3 = max2
                max2 = i
            elif i > max3 and max1 != i and max2 != i:
                max3 = i
            else:
                continue
        if max3 == -2**31 - 1:
            return max1
        else:
            return max3