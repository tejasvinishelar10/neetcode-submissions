class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        L, R = 0, len(heights)-1

        while(L < R):
            water = min(heights[L], heights[R]) * (R-L)
            maxVol = max(maxVol, water)
        
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return maxVol
