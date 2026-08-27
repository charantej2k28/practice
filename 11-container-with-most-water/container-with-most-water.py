class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            h_left = height[left]
            h_right = height[right]
            
            # Calculate current area
            current_area = (right - left) * min(h_left, h_right)
            max_water = max(max_water, current_area)
            
            # Move the pointer with the smaller height inward
            if h_left < h_right:
                left += 1
            else:
                right -= 1
                
        return max_water