from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res_1 = defaultdict(int)
        res_2 = defaultdict(int)
        for char in s:
            res_1[char] += 1
        for char in t:
            res_2[char] += 1
        
        return res_1 == res_2 
        



        