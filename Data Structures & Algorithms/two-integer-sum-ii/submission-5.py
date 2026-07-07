class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            j = i + 1
            second = target - numbers[i]
            if second in numbers:
                while numbers[j] != second:
                    j += 1
                return [i + 1, j + 1]
            
        