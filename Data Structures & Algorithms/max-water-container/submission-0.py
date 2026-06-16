class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        max_water = 0;
        while L < R:
            width = R - L
            h = min(heights[L], heights[R])
            max_water= max(max_water, width * h)

            #move the shorter side inward
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return max_water