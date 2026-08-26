class Solution(object):
    def generateString(self, str1, str2):
        n = len(str1)
        m = len(str2)

        # Length of answer
        length = n + m - 1

        # Initially everything is 'a'
        ans = ['a'] * length

        # fixed[i] = True means this position was fixed by a 'T'
        fixed = [False] * length

        # Step 1: Handle all 'T'
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j

                    # Conflict between two T conditions
                    if fixed[pos] and ans[pos] != str2[j]:
                        return ""

                    ans[pos] = str2[j]
                    fixed[pos] = True

        # Step 2: Handle all 'F'
        for i in range(n):
            if str1[i] == 'F':

                # Check if current substring equals str2
                if ''.join(ans[i:i + m]) == str2:

                    # Break the match using the rightmost
                    # position that wasn't fixed by T
                    changed = False

                    for j in range(i + m - 1, i - 1, -1):
                        if not fixed[j]:
                            ans[j] = 'b'
                            changed = True
                            break

                    # No position can be changed
                    if not changed:
                        return ""

        return ''.join(ans)