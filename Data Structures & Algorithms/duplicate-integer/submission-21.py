class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        num_set = set()

        size = len(nums)

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)

        
        return False
    