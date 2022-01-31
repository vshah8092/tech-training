class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Solution 1
        #d = {}
        #for i in range(len(nums)):
        #    if nums[i] in d:
        #        if abs(i - d[nums[i]]) <= k:
        #            return True
        #    d[nums[i]] = i
        #return False
        
        #Solution 2
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s) > k:
                s.remove(nums[i - k])