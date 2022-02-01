class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        if s - nums[0] == 0:
            return 0
        left = 0
        right = s - nums[0]
        for i in range(1, len(nums) - 1):
            left = left + nums[i - 1]
            right = right - nums[i]
            if left == right:
                return i
        if s - nums[-1] == 0:
            return len(nums) - 1
        return -1