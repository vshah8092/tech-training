class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Solution 1
        #for i in range(len(nums)):
        #    for j in range(i + 1, len(nums)):
        #        if nums[i] + nums[j] == target:
        #            return [i, j]
        
        #Solution 2
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d.keys() and i != d[target - nums[i]]:
                return [i, d[target - nums[i]][0]]
            d[nums[i]] = [i]