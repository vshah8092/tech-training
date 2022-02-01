class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        for i in nums:
            if i != m and 2 * i > m:
                return -1
        return nums.index(m)