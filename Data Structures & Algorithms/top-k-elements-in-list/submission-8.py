from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        arr = [[] for i in range(len(nums) + 1)]
        result = []
        for num in nums:
            res[num] += 1
        for n, c in res.items():
            arr[c].append(n)
        for lst in arr[::-1]:
            for n in lst:
                result.append(n)
            if len(result) == k:
                return result
                    
        

        
            


