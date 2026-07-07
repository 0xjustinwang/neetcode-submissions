from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        longest = 0
        for n in res:
            count = 0
            if (n - 1) not in res:
                while (n + count) in res:
                    count += 1
                longest = max(longest, count)
        return longest