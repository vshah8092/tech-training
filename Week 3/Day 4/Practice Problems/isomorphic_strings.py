class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        d = {}
        string = ""
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            string += d[s[i]]
        if string == t:
            return True
        return False