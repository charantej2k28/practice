from collections import Counter


class Solution(object):

    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        total_counts = Counter(s)

        # Precompute prefix counts of target to quickly check feasibility
        prefix_counts = [Counter()]
        for ch in target:
            new_count = prefix_counts[-1].copy()
            new_count[ch] += 1
            prefix_counts.append(new_count)

        # Iterate from the longest possible matching prefix down to 0
        for i in range(n - 1, -1, -1):
            req = prefix_counts[i]

            # Check if target[:i] can be formed using characters from s
            if all(total_counts[ch] >= req[ch] for ch in req):
                # Calculate available characters remaining for position i and beyond
                remaining = total_counts.copy()
                remaining.subtract(req)

                # Find the smallest available character strictly greater than target[i]
                target_char = target[i]
                for char_code in range(ord(target_char) + 1, ord("z") + 1):
                    c = chr(char_code)
                    if remaining[c] > 0:
                        remaining[c] -= 1

                        # Construct suffix with the rest of the characters in ascending order
                        suffix = "".join(
                            sorted(
                                ch * cnt
                                for ch, cnt in remaining.items()
                                if cnt > 0
                            )
                        )
                        return target[:i] + c + suffix

        return ""