class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_dup = set()

        for num in nums:
            if num in n_dup:
                return True
            n_dup.add(num)
            
        
        return False