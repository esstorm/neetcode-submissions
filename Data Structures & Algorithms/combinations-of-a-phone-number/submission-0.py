class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": "",
        }

        if digits == "":
            return []
        
        return ["".join(x) for x in product(*[chars[digit] for digit in digits])]