class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Find the closest point in the rectangle to the circle center
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        # Calculate squared distance
        dx = xCenter - closestX
        dy = yCenter - closestY

        # Compare with radius squared
        return dx * dx + dy * dy <= radius * radius