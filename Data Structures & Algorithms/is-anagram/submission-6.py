class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}

        s_size = len(s)
        t_size = len(t)
        
        if s_size != t_size:
            return False

        for i in range(s_size):
            if s not in s_set:
                s_set[s[i]] = 1 + s_set.get(s[i], 0)
                t_set[t[i]] = 1 + t_set.get(t[i],0)

            
        for c in s_set:
            if s_set[c] != t_set.get(c,0):
                return False 

        return True 