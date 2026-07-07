from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = defaultdict(set)
        if not nums:
            return 0
        for i in range(len(nums)):
            val = nums[i]
            if val - 1 not in nums:
                res[val] = {val}
            j = 0
            while val + j in nums:
                res[val].add(val + j)
                j += 1
            
        return len(max(res.values(), key=len))
