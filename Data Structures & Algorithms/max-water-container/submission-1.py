class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        for i in range(len(heights)):
            for j in range(1, len(heights)):
                delta = j - i 
                height = min(heights[i], heights[j])
                maxA = max(maxA, delta * height)
        return maxA