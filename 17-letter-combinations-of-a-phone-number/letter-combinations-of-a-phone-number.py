class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(index, current_combo):
            if index == len(digits):
                res.append("".join(current_combo))
                return

            letters = phone_map[digits[index]]
            for letter in letters:
                current_combo.append(letter)
                backtrack(index + 1, current_combo)
                current_combo.pop()

        backtrack(0, [])
        return res