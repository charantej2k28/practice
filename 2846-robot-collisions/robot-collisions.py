class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        n = len(positions)
        # Sort robot indices by their initial positions
        indices = sorted(range(n), key=lambda i: positions[i])
        
        stack = []  # Stores indices of surviving 'R' moving robots
        
        for curr in indices:
            if directions[curr] == 'R':
                stack.append(curr)
            else:
                # The current robot is moving 'L' and collides with 'R' robots in stack
                while stack and healths[curr] > 0:
                    top = stack[-1]
                    
                    if healths[curr] > healths[top]:
                        # 'R' robot dies, 'L' robot loses 1 health and continues
                        healths[top] = 0
                        healths[curr] -= 1
                        stack.pop()
                    elif healths[curr] < healths[top]:
                        # 'L' robot dies, 'R' robot loses 1 health and stays on stack
                        healths[curr] = 0
                        healths[top] -= 1
                    else:
                        # Both robots die
                        healths[curr] = 0
                        healths[top] = 0
                        stack.pop()
        
        # Return remaining healths of surviving robots in their original order
        return [h for h in healths if h > 0]