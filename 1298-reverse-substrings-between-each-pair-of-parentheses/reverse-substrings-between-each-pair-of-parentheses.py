class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                temp = []

                # Get characters inside the parentheses
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())

                # Remove '('
                stack.pop()

                # temp is already reversed because of popping
                stack.extend(temp)

        return ''.join(stack)