class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        lst = []
        for i in range(len(nums)):
            if nums[i] in res:
                if i < res[nums[i]]:
                    lst.extend([i] + [res[nums[i]]])
                else:
                    lst.extend([res[nums[i]]] + [i])
            difference = target - nums[i]
            if difference not in res:
                res[difference] = i 
        return lst
                    
