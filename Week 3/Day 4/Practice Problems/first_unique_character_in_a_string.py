class Solution:
    def firstUniqChar(self, s: str) -> int:
        #Solution 1
        #d = {}
        #for i in range(len(s)):
        #    if s[i] in d:
        #        d[s[i]][1] += 1
        #    else:
        #        d[s[i]] = [i, 1]
        #a = list(d.values())
        #a.sort(key = lambda x:x[1])
        #min = 100000
        #for i in a:
        #    if i[1] == 1:
        #        if min > i[0]:
        #            min = i[0]
        #        else:
        #            break
        #if min == 100000:
        #    return -1
        #return min
        
        #Solution 2
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1