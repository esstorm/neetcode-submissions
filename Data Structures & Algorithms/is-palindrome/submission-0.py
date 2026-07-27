class Solution:
    def isPalindrome(self, s: str) -> bool:
        proc = "".join(list(filter(lambda x: x.isalnum(), s.lower())))

        return proc == proc[::-1]
        