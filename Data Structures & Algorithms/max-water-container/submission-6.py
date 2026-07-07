class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        O(n^2)
        '''
        # maxA = 0
        # for i in range(len(heights)):
        #     for j in range(1, len(heights)):
        #         delta = j - i 
        #         height = min(heights[i], heights[j])
        #         maxA = max(maxA, delta * height)
        # return maxA
        
        i, j = 0, len(heights) - 1
        maxA = 0
        while i < j:
            left, right = heights[i], heights[j]
            height = min(left, right)
            delta = j - i 
            maxA = max(maxA, height * delta)
            if left > right:
                j -= 1
            else:
                i += 1
        return maxA

        
