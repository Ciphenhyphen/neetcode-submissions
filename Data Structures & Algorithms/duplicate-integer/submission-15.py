class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for every num in a list
        # compare the first number with the rest
        # Use a set for no duplicates
        n_dup = set()

        for n in nums:
            if n in n_dup:
                return True
            n_dup.add(n)
        return False
    