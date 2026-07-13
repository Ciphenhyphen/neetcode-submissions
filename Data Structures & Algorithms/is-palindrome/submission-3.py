class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # For every letter in a word, 
        # if the character in front and back are the same, continue
        # else, return false. 
       
        # Ignore everything not alphanumeric then
        # Validate the letter at the ith point, 
        # If true, move them forward/backward
        # else, return false

        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]