class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        i = 0
        n = len(words)

        while i < n:
            line = [words[i]]
            line_len = len(words[i])
            i += 1

            # Greedily include as many words as can fit with at least 1 space between them
            while i < n and line_len + 1 + len(words[i]) <= maxWidth:
                line.append(words[i])
                line_len += 1 + len(words[i])
                i += 1

            # Case 1: Last line or single-word line -> Left-justify
            if i == n or len(line) == 1:
                left_justified = " ".join(line)
                result.append(left_justified.ljust(maxWidth))
            else:
                # Case 2: Fully justify
                total_letters = sum(len(w) for w in line)
                total_spaces = maxWidth - total_letters
                num_gaps = len(line) - 1

                base_spaces = total_spaces // num_gaps
                extra_spaces = total_spaces % num_gaps

                # Construct line by adding spaces between words
                line_str = []
                for j in range(num_gaps):
                    line_str.append(line[j])
                    # Add base spaces + 1 extra space if it falls in the leftmost gaps
                    spaces_to_add = base_spaces + (1 if j < extra_spaces else 0)
                    line_str.append(" " * spaces_to_add)

                line_str.append(line[-1])  # Append the final word
                result.append("".join(line_str))

        return result