class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                currSum = num + nums[j] + nums[k]
                if currSum < 0:
                    j += 1
                elif currSum > 0:
                    k -= 1
                else:
                    res.append([num, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res


