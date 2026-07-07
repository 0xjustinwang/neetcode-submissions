class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        for i, num in enumerate(nums):
            new = nums[:]
            new.remove(num)
            product = 1
            for n in new:
                product = product * n
            arr[i] = product
        return arr