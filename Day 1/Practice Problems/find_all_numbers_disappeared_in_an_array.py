class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #Solution 1
        #nums1 = set(nums)
        #l = []
        #for i in range(1, len(nums) + 1):
        #    if i not in nums1:
        #        l.append(i)
        #return l
        
        #Solution 2
        l = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]
        for i in range(len(nums)):
            if nums[i] > 0:
                l.append(i + 1)
        return l