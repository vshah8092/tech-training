class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Solution 1
        #ans = []
        #if len(nums1) > len(nums2):
        #    nums1, nums2 = nums2, nums1
        #for i in range(len(nums1)):
        #    if nums1[i] in nums2:
        #        ans.append(nums1[i])
        #return list(set(ans))
        
        #Solution 2
        #s = set()
        #nums1.sort()
        #nums2.sort()
        #i = 0
        #j = 0
        #while i < len(nums1) and j < len(nums2):
        #    if nums1[i] > nums2[j]:
        #        j += 1
        #    elif nums1[i] < nums2[j]:
        #        i += 1
        #    else:
        #        s.add(nums1[i])
        #        i += 1
        #        j += 1
        #return list(s)
        
        #Solution 3
        d = {}
        l = []
        for i in nums1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in nums2:
            if i in d and d[i] > 0:
                l.append(i)
                d[i] -= 1
        return l