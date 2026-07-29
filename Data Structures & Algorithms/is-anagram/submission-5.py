class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # For this one, I believe you would:
        # Take a letter, confirm it exists in the other string
        # repeat the process until all letters in one string match the other

        # Be sure they're equal lengthwise, else it's false

        # Maybe rebuild the string?
        t_size = len(t)
        s_size = len(s)

        if s_size != t_size:
            return False

        t_set = {}
        s_set = {}
        for i in range (s_size):
            s_set[s[i]] = 1 + s_set.get(s[i], 0)
            t_set[t[i]] = 1 + t_set.get(t[i], 0)
        
        for c in s_set:
            if s_set[c] != t_set.get(c,0):
                return False
        


        return True 