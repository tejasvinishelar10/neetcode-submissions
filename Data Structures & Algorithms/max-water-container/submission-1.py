class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        max_water = 0
        while(L < R):
            total_water = min(heights[L], heights[R]) * (R-L)
            max_water = max(max_water, total_water)

            if(heights[L] < heights[R]):
                L += 1
            else:
                R -= 1
        return max_water