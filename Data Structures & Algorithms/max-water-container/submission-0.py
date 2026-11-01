class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        biggest_area = 0

        while start <= end:
            curr_area = (end - start) * min(heights[start], heights[end])

            if heights[start] < heights[end]:
                start+=1
            else:
                end-= 1
            biggest_area = max(biggest_area, curr_area)
        return biggest_area          
