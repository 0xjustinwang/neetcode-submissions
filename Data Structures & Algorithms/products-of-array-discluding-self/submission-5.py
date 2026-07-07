class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        for i in range(len(nums)):
            new = nums[:]
            new.pop(i)
            product = 1
            for n in new:
                product = product * n
            arr[i] = product
        return arr