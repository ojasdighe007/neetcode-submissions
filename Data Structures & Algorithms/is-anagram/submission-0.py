class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))

        n = len(s)
        m = len(t)

        if n != m:
            return False
        
        for i in range(0,n):
            if s[i] != t[i]:
                return False
        
        return True