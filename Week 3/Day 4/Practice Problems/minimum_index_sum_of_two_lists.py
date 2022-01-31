class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        min = 2000
        for i in range(len(list1)):
            d[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in d:
                if d[list2[j]] + j < min:
                    min = d[list2[j]] + j
                    ans = [list2[j]]
                elif d[list2[j]] + j == min:
                    ans.append(list2[j])
                else:
                    continue
        return ans