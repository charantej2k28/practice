class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        tokens = path.split('/')
        
        for token in tokens:
            if token == '' or token == '.':
                continue
            elif token == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(token)
                
        return '/' + '/'.join(stack)